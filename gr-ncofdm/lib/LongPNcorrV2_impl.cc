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
#include "LongPNcorrV2_impl.h"

int Update_counter = 0;
int pksaved = 0;
namespace gr {
  namespace ncofdm {

    LongPNcorrV2::sptr
    LongPNcorrV2::make(int fft_len, int cp_len, int LgSeqLen, const std::vector<gr_complex> &LgSeq, float LgThres, int UpdateInterval)
    {
      return gnuradio::get_initial_sptr
        (new LongPNcorrV2_impl(fft_len, cp_len, LgSeqLen, LgSeq, LgThres, UpdateInterval));
    }

    /*
     * The private constructor
     */
    LongPNcorrV2_impl::LongPNcorrV2_impl(int fft_len, int cp_len, int LgSeqLen, const std::vector<gr_complex> &LgSeq, float LgThres, int UpdateInterval)
      : gr::sync_block("LongPNcorrV2",
                    gr::io_signature::make3(3, 3, sizeof(gr_complex), sizeof(gr_complex), sizeof(float)),
                    gr::io_signature::make3(3, 3, sizeof(gr_complex), sizeof(gr_complex), sizeof(int))),
                    d_fft_len(fft_len),
                    d_cp_len(cp_len),
                    d_LgSeqLen(LgSeqLen),
                    d_symbols(LgSeq),           
                    d_LgThres(LgThres),
                    d_UpdateInterval(UpdateInterval)
        {
            std::reverse(d_symbols.begin(), d_symbols.end());
            d_filter = new filter::kernel::fft_filter_ccc(1, d_symbols);
            set_history(d_filter->ntaps());
            set_output_multiple(d_symbols.size());            
        }

    /*
     * Our virtual destructor.
     */
    LongPNcorrV2_impl::~LongPNcorrV2_impl()
    {
    }

    int
    LongPNcorrV2_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
                const gr_complex *in = (const gr_complex *) input_items[0];
                const gr_complex *fl_fos = (const gr_complex *) input_items[1];
                const float *movavg = (const float *) input_items[2];
                gr_complex *out = (gr_complex *) output_items[0];
                gr_complex *corr = (gr_complex *) output_items[1];
                int *flag = (int *) output_items[2];

                //gr_complex longcorr;

                // Do <+signal processing+>
                //memcpy(out, in, sizeof(gr_complex)*noutput_items);        
                // d_filter->filter(noutput_items, in, corr);

                // Avoid buffer overflow from nested while, putting a stopper at the end

                for(int i=0; i<noutput_items; i++){
                    flag[i] = 0;
                    d_longcorr = (0,0);
                    out[i].real() = d_LgThres;
                    out[i].imag() = 0;
                    if (real(fl_fos[i]) > 0){
                        for (int j=i; j<i+d_LgSeqLen; j++){
                            d_fos.real() = (cos(2*3.14159265*imag(fl_fos[i])*(j-i)));
                            d_fos.imag() = (sin(2*3.14159265*imag(fl_fos[i])*(j-i)));
                            d_longcorr = d_longcorr +in[j] * d_fos * d_symbols[history()-(j-i)-1];
                        }
                        if (abs(d_longcorr) > d_LgThres){
                            flag[i] = 1;
                            if (abs(d_longcorr)>pksaved)
                                pksaved = abs(d_longcorr);  // Save the peak
                        }
                    }
                    corr[i] = d_longcorr;
                    Update_counter++;
                    int tempLgThres;
                    if ((Update_counter % d_UpdateInterval) - d_LgSeqLen == 0){
                        if(pksaved > 0){
                            tempLgThres = pksaved;
                        }
                        else{
                            tempLgThres = movavg[i]*d_LgSeqLen/3.4641; //sqrt(12)=3.4641
                        }
                        d_LgThres = 0.7*d_LgThres +0.3*0.8*tempLgThres;
                        pksaved = 0;
                    }
                    if (Update_counter == d_UpdateInterval)
                        Update_counter = 0;
                }

                //std::cout << ++temp_counter << "###" << noutput_items<< std::endl;
                // Tell runtime system how many output items we produced.
                return noutput_items;
    }

  } /* namespace ncofdm */
} /* namespace gr */

