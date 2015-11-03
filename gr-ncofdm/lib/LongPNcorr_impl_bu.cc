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
#include "LongPNcorr_impl.h"
#include <volk/volk.h>

namespace gr {
    namespace ncofdm {

        LongPNcorr::sptr
            LongPNcorr::make(
                    int fft_len, 
                    int cp_len, 
                    int LgSeqLen, 
                    const std::vector<gr_complex> &LgSeq
                    )
            {
                return gnuradio::get_initial_sptr
                    (new LongPNcorr_impl(fft_len, cp_len, LgSeqLen, LgSeq));
            }

        /*
         * The private constructor
         */
        LongPNcorr_impl::LongPNcorr_impl(int fft_len, int cp_len, int LgSeqLen, const std::vector<gr_complex> &LgSeq)
            : gr::sync_block("LongPNcorr",
                    gr::io_signature::make2(2, 2, sizeof(gr_complex), sizeof(int)),
                    gr::io_signature::make3(3, 3, sizeof(gr_complex), sizeof(gr_complex), sizeof(int))),
                    d_fft_len(fft_len),
                    d_cp_len(cp_len),
                    d_LgSeqLen(LgSeqLen),
                    d_symbols(LgSeq)            
        {
            std::reverse(d_symbols.begin(), d_symbols.end());
            d_filter = new filter::kernel::fft_filter_ccc(1, d_symbols);
            set_history(d_filter->ntaps());
            set_output_multiple(d_symbols.size());            
        }

        /*
         * Our virtual destructor.
         */
        LongPNcorr_impl::~LongPNcorr_impl()
        {
        }

        int
            LongPNcorr_impl::work(int noutput_items,
                    gr_vector_const_void_star &input_items,
                    gr_vector_void_star &output_items)
            {
                const gr_complex *in = (const gr_complex *) input_items[0];
                const int *rxflag = (const int *) input_items[1];
                gr_complex *out = (gr_complex *) output_items[0];
                gr_complex *corr = (gr_complex *) output_items[1];
                int *flag = (int *) output_items[2];

                // Do <+signal processing+>
                memcpy(out, in, sizeof(gr_complex)*noutput_items);        
                d_filter->filter(noutput_items, in, corr);
                // Find the magnitude squared of the correlation
                std::vector<float> corr_mag(noutput_items);
                volk_32fc_magnitude_32f(&corr_mag[0], corr, noutput_items);

                // Avoid buffer overflow from nested while, putting a stopper at the end
                corr_mag[noutput_items]=0;	

                for(int i=1; i<noutput_items+1; i++){
                    flag[i-1] = 0;
                    if (rxflag[i-1] > 0){
                        //if (corr_mag[i] > 0.04*d_LgSeqLen*d_LgSeqLen){
                        if (corr_mag[i] > 40){
                            flag[i-1] = 1;
                        }
                    }
                }


                // Tell runtime system how many output items we produced.
                return noutput_items;
            }

    } /* namespace ncofdm */
} /* namespace gr */


