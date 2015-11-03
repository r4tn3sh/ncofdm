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
#include "ShortPNdetector_impl.h"

namespace gr {
    namespace ncofdm {

        ShortPNdetector::sptr
            ShortPNdetector::make(int fft_len, int cp_len, int ShSeqRep, int ShSeqLen, float threshold)
            {
                return gnuradio::get_initial_sptr
                    (new ShortPNdetector_impl(fft_len, cp_len, ShSeqRep, ShSeqLen, threshold));
            }

        /*
         * The private constructor
         */
        ShortPNdetector_impl::ShortPNdetector_impl(int fft_len, int cp_len, int ShSeqRep, int ShSeqLen, float threshold)
            : gr::sync_block("ShortPNdetector",
                    gr::io_signature::make(1, 1, sizeof(float)),
                    gr::io_signature::make(2, 2, sizeof(float))),
            d_fft_len(fft_len),
            d_cp_len(cp_len),
            d_ShSeqRep(ShSeqRep),
            d_ShSeqLen(ShSeqLen),
            d_threshold(threshold)
        {
            int TotalLen = d_ShSeqRep*d_ShSeqLen;
            std::vector<float> filtertaps(TotalLen);
            for(int i = 0; i<TotalLen; i++){
                filtertaps[i] = 0.0; 
                if (i%d_ShSeqLen == d_ShSeqLen-1)
                    filtertaps[i] = 1.0;
            }
            //std::reverse(filtertaps.begin(), filtertaps.end());
            d_filter = new filter::kernel::fft_filter_fff(1, filtertaps);
            //set_history(d_filter->ntaps());
            set_history(d_ShSeqLen*(d_ShSeqRep-1));
            set_output_multiple(TotalLen);            
            message_port_register_in(pmt::mp("threshold"));
            set_msg_handler(
                    pmt::mp("threshold"), 
                    boost::bind(&ShortPNdetector_impl::process_msg, this, _1)
                    );
        }

        /*
         * Our virtual destructor.
         */
        ShortPNdetector_impl::~ShortPNdetector_impl()
        {
            delete d_filter;
        }

        void ShortPNdetector_impl::process_msg(pmt::pmt_t msg){
            float tempvar = pmt::to_float(msg);
            d_threshold = tempvar;
        }

        int
            ShortPNdetector_impl::work(int noutput_items,
                    gr_vector_const_void_star &input_items,
                    gr_vector_void_star &output_items)
            {
                const float *in = (const float *) input_items[0];
                float *out = (float *) output_items[0];
                float *thresh = (float *) output_items[1];

                // Do <+signal processing+>
                temp_in = new float[noutput_items+history()];
                //std::cout << d_threshold << std::endl;
                for (int i=0; i<noutput_items+history(); i++){
                    if (i<noutput_items)
                        thresh[i] = d_threshold;
                    if (in[i]>d_threshold)
                        temp_in[i] = 1;
                    else
                        temp_in[i] = 0;
                }
                // d_filter->filter(noutput_items, in, out);
                for (int i=0; i<noutput_items; i++){
                    out[i] = 0;
                    for (int j=0; j<d_ShSeqRep; j++){
                        out[i] = out[i] + temp_in[i+j*d_ShSeqLen];
                    }
                }

                delete temp_in;
                // Tell runtime system how many output items we produced.
                return noutput_items;
            }

    } /* namespace ncofdm */
} /* namespace gr */

