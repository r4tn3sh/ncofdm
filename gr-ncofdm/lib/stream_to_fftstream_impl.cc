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
#include "stream_to_fftstream_impl.h"

namespace gr {
    namespace ncofdm {

        stream_to_fftstream::sptr
            stream_to_fftstream::make(int fft_len, int cp_len)
            {
                return gnuradio::get_initial_sptr
                    (new stream_to_fftstream_impl(fft_len, cp_len));
            }

        /*
         * The private constructor
         */
        stream_to_fftstream_impl::stream_to_fftstream_impl(int fft_len, int cp_len)
            : gr::block("stream_to_fftstream",
                    gr::io_signature::make2(2, 2, sizeof(gr_complex), sizeof(int)),
                    gr::io_signature::make(1, 1, sizeof(gr_complex))),
            d_fft_len(fft_len),
            d_cp_len(cp_len)
        {
            if (d_cp_len > d_fft_len){
                throw std::invalid_argument("CP Length can not be less than FFT length");
            }
            if (d_cp_len<1 || d_fft_len<1){
                throw std::invalid_argument("CP Length or FFT length should be positive integers");
            }

            float io_ratio;
            io_ratio = (d_fft_len + d_cp_len)/d_fft_len;
            //set_history(d_fft_len+d_cp_len);
            set_output_multiple(d_fft_len);
            set_relative_rate(static_cast<double>(d_fft_len)/static_cast<double>(d_fft_len+d_cp_len));
            //set_relative_rate(io_ratio);
        }

        /*
         * Our virtual destructor.
         */
        stream_to_fftstream_impl::~stream_to_fftstream_impl()
        {
        }

        void
            stream_to_fftstream_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
            {
                unsigned ninputs = ninput_items_required.size();
                for(unsigned i = 0; i < ninputs; i++){
                    ninput_items_required[i] = noutput_items * (d_fft_len+d_cp_len)/d_fft_len;
                }
            }

        int
            stream_to_fftstream_impl::general_work (int noutput_items,
                    gr_vector_int &ninput_items,
                    gr_vector_const_void_star &input_items,
                    gr_vector_void_star &output_items)
            {
                const gr_complex *in = (const gr_complex *) input_items[0];
                const int *flag = (const int *) input_items[1];
                gr_complex *out = (gr_complex *) output_items[0];

                static unsigned int blkcnt = 0;
                static unsigned int index = 0;

                unsigned int outindex = 0;
                int min_in_items = std::min(ninput_items[0], ninput_items[1]);
                int blks = std::min(noutput_items/d_fft_len, min_in_items/(d_fft_len+d_cp_len));
                //std::cout << noutput_items << "# " << ninput_items[0] <<  "# " << ninput_items[1] <<"# " << blks*(d_fft_len+d_cp_len) << std::endl;
                //for (int i = 0; i<noutput_items * (d_fft_len+d_cp_len); i++){
                for (int i = 0; i<blks*(d_fft_len+d_cp_len); i++){
                    // Check if an fft boundry flag was detected
                    if (flag[i] > 0){
                        blkcnt = 0;
                        index = 0;
                    }
                    else if ((blkcnt%(d_fft_len+d_cp_len))==0){
                        index = 0;
                    }

                    // Select the data of fft length
                    out[outindex] = 0;
                    if (index >= d_cp_len){
                        out[outindex++] = in[i];
                    }
                    blkcnt++;
                    index++;
                }
                // Increment the pointers
                in += blks*(d_fft_len+d_cp_len);
                out += outindex;

                // Tell runtime system how many input items we consumed on
                // each input stream.
                consume_each(blks*(d_fft_len+d_cp_len));

                // Tell runtime system how many output items we produced.
                return noutput_items;
            }

    } /* namespace ncofdm */
} /* namespace gr */

