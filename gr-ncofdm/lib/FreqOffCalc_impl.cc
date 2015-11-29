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

#define PI 3.14159265
#include <gnuradio/io_signature.h>
#include "FreqOffCalc_impl.h"

namespace gr {
  namespace ncofdm {

    FreqOffCalc::sptr
    FreqOffCalc::make(int fft_len, int cp_len, int ShSeqLen, int ShSeqRep)
    {
      return gnuradio::get_initial_sptr
        (new FreqOffCalc_impl(fft_len, cp_len, ShSeqLen, ShSeqRep));
    }

    /*
     * The private constructor
     */
    FreqOffCalc_impl::FreqOffCalc_impl(int fft_len, int cp_len, int ShSeqLen, int ShSeqRep)
      : gr::sync_block("FreqOffCalc",
              gr::io_signature::make2(2, 2, sizeof(gr_complex), sizeof(int)),
              gr::io_signature::make(1, 1, sizeof(float))),
            d_fft_len(fft_len),
            d_cp_len(cp_len),
            d_ShSeqRep(ShSeqRep),
            d_ShSeqLen(ShSeqLen)
    {
        set_history(d_ShSeqRep*d_ShSeqLen);
        set_output_multiple(d_ShSeqRep*d_ShSeqLen);            
	}

    /*
     * Our virtual destructor.
     */
    FreqOffCalc_impl::~FreqOffCalc_impl()
    {
    }

    int
    FreqOffCalc_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const gr_complex *in = (const gr_complex *) input_items[0];
        const int *rxflag = (const int *) input_items[1];
        float *out = (float *) output_items[0];

        // Do <+signal processing+>
        gr_complex diff_in;
        float diff_angle;
        for (int i=history(); i<noutput_items+history(); i++){
            out[i-history()] = 0;
            if (rxflag[i]>0){
                offset = 0;
                for (int j=0; j<d_ShSeqRep-1; j++){
                    diff_in = in[i-(j+1)*d_ShSeqLen]/in[i-j*d_ShSeqLen];
                    angle1 = atan2(in[i-j*d_ShSeqLen].imag(), in[i-j*d_ShSeqLen].real());
                    angle2 = atan2(in[i-(j+1)*d_ShSeqLen].imag(), in[i-(j+1)*d_ShSeqLen].real());
                    //diff_angle = angle2-angle1;
                    diff_angle = atan2(diff_in.imag(), diff_in.real());
                    offset = offset + (diff_angle)/(2*PI*d_ShSeqLen);
                    /*
                    if (diff_angle > PI)
                        offset = offset + (2*PI-(diff_angle))/(2*PI*d_ShSeqLen);
                    else if (angle2-angle1 < -PI)
                        offset = offset + (2*PI+(diff_angle))/(2*PI*d_ShSeqLen);
                    else
                        offset = offset + (diff_angle)/(2*PI*d_ShSeqLen);
                    */
                }
                out[i-history()] = offset/(d_ShSeqRep-1);
                //std::cout << out[i-history()] <<"******" << std::endl;
            }
        }

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace ncofdm */
} /* namespace gr */

