/* -*- c++ -*- */
/* 
 * Copyright 2015 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include <gnuradio/blocks/conjugate_cc.h>
#include "underlay_sync_detector_impl.h"
#include <volk/volk.h>
#include <boost/format.hpp>

namespace gr {
    namespace ncofdm {

        underlay_sync_detector::sptr
            underlay_sync_detector::make(size_t input_size, size_t output_size, int sync_len, const std::vector<gr_complex> &symbols)
            {
                return gnuradio::get_initial_sptr
                    (new underlay_sync_detector_impl(input_size, output_size, sync_len, symbols));
            }

        /*
         * The private constructor
         */
        underlay_sync_detector_impl::underlay_sync_detector_impl(size_t input_size, size_t output_size, int sync_len, const std::vector<gr_complex> &symbols)
            : gr::sync_block("underlay_sync_detector",
                    gr::io_signature::make(1, 1, sizeof(gr_complex)),
                    gr::io_signature::make(2, 2, sizeof(gr_complex))),
            d_fft_len(input_size),
            d_output_size(output_size),
            d_symbols(symbols),
            d_sync_len(sync_len) 
                //gr::io_signature::make2(2, 2, sizeof(gr_complex), sizeof(float)))
        {
            //set_symbols(symbols);
            
            d_symbols.resize(sync_len*output_size);
            std::reverse(d_symbols.begin(), d_symbols.end());
            d_filter = new filter::kernel::fft_filter_ccc(1, d_symbols);
            set_history(d_symbols.size());
            set_output_multiple(d_symbols.size());
            //set_history(d_symbols.size());
            /*const int alignment_multiple =
                volk_get_alignment() / sizeof(gr_complex);
            set_alignment(std::max(1,alignment_multiple));
            */
        }

        /*
         * Our virtual destructor.
         */
        underlay_sync_detector_impl::~underlay_sync_detector_impl()
        {
            delete d_filter;
        }

        void
            underlay_sync_detector_impl::set_symbols(const std::vector<gr_complex> &symbols)
            {
                //gr::thread::scoped_lock lock(d_setlock);
                d_symbols = symbols;
                //d_filter->set_taps(symbols);
                //set_history(d_filter->ntaps());
            }

        int
            underlay_sync_detector_impl::work(int noutput_items,
                    gr_vector_const_void_star &input_items,
                    gr_vector_void_star &output_items)
            {
                const gr_complex *in = (gr_complex *) input_items[0];
                gr_complex *out = (gr_complex *) output_items[0];
                //float *corr = (float*)output_items[1];
                gr_complex *corr_cp = (gr_complex*)output_items[1];


                memcpy(out, in, sizeof(gr_complex)*noutput_items);
                float *abs_in;
                abs_in = new float[noutput_items];
                volk_32fc_magnitude_32f_u(abs_in, in, noutput_items);

                // Calculating average power in the block
                float avg_pwr = 0;
                for(int i=0; i<noutput_items; i++){
                    avg_pwr = avg_pwr + abs_in[i]*abs_in[i];
                }
                delete abs_in;
                avg_pwr = avg_pwr/noutput_items;
                avg_pwr = 1;

                gr_complex *fil_in;
                fil_in = new gr_complex[noutput_items];
                for(int i=0; i<noutput_items; i++){
                    fil_in[i] = in[i]/avg_pwr;
                }
                //std::vector<gr_complex> corr_cp(noutput_items+1);
                d_filter->filter(noutput_items, fil_in, corr_cp);
                delete fil_in;

                // Tell runtime system how many output items we produced.
                //std::cout << noutput_items << "; ";
                return noutput_items;
            }

    } /* namespace ncofdm */
} /* namespace gr */

