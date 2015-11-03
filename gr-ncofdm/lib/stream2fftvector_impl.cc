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
#include "stream2fftvector_impl.h"

unsigned int blkcnt = 0;
namespace gr {
    namespace ncofdm {

        stream2fftvector::sptr
            stream2fftvector::make(int fft_len, int cp_len)
            {
                return gnuradio::get_initial_sptr
                    (new stream2fftvector_impl(fft_len, cp_len));
            }

        /*
         * The private constructor
         */
        stream2fftvector_impl::stream2fftvector_impl(int fft_len, int cp_len)
            : gr::block("stream2fftvector",
                    gr::io_signature::make2(2, 2, sizeof(gr_complex), sizeof(int)),
                    gr::io_signature::make(1, 1, sizeof(gr_complex)*fft_len)),
            d_fft_len(fft_len),
            d_cp_len(cp_len)
        {
            set_history(d_fft_len+d_cp_len);
        }

        /*
         * Our virtual destructor.
         */
        stream2fftvector_impl::~stream2fftvector_impl()
        {
        }

        void
            stream2fftvector_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
            {
                ninput_items_required[0] = noutput_items * (d_fft_len+d_cp_len);
            }

        int
            stream2fftvector_impl::general_work (int noutput_items,
                    gr_vector_int &ninput_items,
                    gr_vector_const_void_star &input_items,
                    gr_vector_void_star &output_items)
            {
                const gr_complex *in = (const gr_complex *) input_items[0];
                const int *flag = (const int *) input_items[1];
                gr_complex *out = (gr_complex *) output_items[0];

                // Do <+signal processing+>
                unsigned int index;
                unsigned int outindex = 0;
                for (int i = 0; i<noutput_items * (d_fft_len+d_cp_len); i++){
                    if (flag[i] > 0){
                        blkcnt = 0;
                        index = 0;
                    }
                    else if ((blkcnt%(d_fft_len+d_cp_len))==0){
                        index = 0;
                    }

                    if (index<d_fft_len){
                        out[outindex++] = in[i + d_cp_len + 1];
                    }
                }
                // Tell runtime system how many input items we consumed on
                // each input stream.
                consume_each (noutput_items * (d_fft_len+d_cp_len));

                // Tell runtime system how many output items we produced.
                return noutput_items;
            }

    } /* namespace ncofdm */
} /* namespace gr */

