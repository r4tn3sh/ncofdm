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

#include <iostream>     // std::cout
#include <algorithm>    // std::sort
#include <vector> 
#include <gnuradio/io_signature.h>
#include "DyThresAdjust_impl.h"

int UpdateCounter = 0;
int LgPeakRxd = 0;

namespace gr {
  namespace ncofdm {

    DyThresAdjust::sptr
    DyThresAdjust::make(int ShSeqLen, int ShSeqRep, int LgSeqLen, float ShThres, float LgThres, int UpdatePeriod)
    {
      return gnuradio::get_initial_sptr
        (new DyThresAdjust_impl(ShSeqLen, ShSeqRep, LgSeqLen, ShThres, LgThres, UpdatePeriod));
    }

    /*
     * The private constructor
     */
    DyThresAdjust_impl::DyThresAdjust_impl(int ShSeqLen, int ShSeqRep, int LgSeqLen, float ShThres, float LgThres, int UpdatePeriod)
      : gr::sync_block("DyThresAdjust",
              gr::io_signature::make(4, 4, sizeof(float)),
              gr::io_signature::make(2, 2, sizeof(float))),
                    d_ShSeqLen(ShSeqLen),
                    d_ShSeqRep(ShSeqRep),
                    d_LgSeqLen(LgSeqLen),
                    d_ShThres(ShThres),
                    d_LgThres(LgThres),
                    d_UpdatePeriod(UpdatePeriod)
    {
        message_port_register_out(pmt::mp("out_sh"));
        message_port_register_out(pmt::mp("out_lg"));
        set_history(d_ShSeqLen*(d_ShSeqRep-1));
    }

    /*
     * Our virtual destructor.
     */
    DyThresAdjust_impl::~DyThresAdjust_impl()
    {
    }

    int
    DyThresAdjust_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const float *ShCorr = (const float *) input_items[0]; // output from short seq correlator
        const float *LgCorr = (const float *) input_items[1]; // output from long seq correlator
        const float *LgFlag = (const float *) input_items[2]; // Final peak detection info (binary)
        const float *MovAvgData = (const float *) input_items[3]; // Moving average of incoming data
        float *shth = (float *) output_items[0];
        float *lgth = (float *) output_items[1];

        // Do <+signal processing+>
        int Peak2Pick;
        float ShPeakArr[d_ShSeqRep];
        for (int i=history(); i<noutput_items+history(); i++){
            // Is a peak detected from long sequence?
            if (LgFlag[i] > 0){
                if (LgCorr[i]>LgPeakRxd)
                    LgPeakRxd = LgCorr[i];  // Save the peak
                Peak2Pick = ceil(d_ShSeqRep*0.5)-1;
                for (int j=0; j<d_ShSeqRep; j++){
                        ShPeakArr[j] = ShCorr[i-j*d_ShSeqLen];
                }
                std::vector<float> myvector (ShPeakArr, ShPeakArr+d_ShSeqRep);
                std::sort (myvector.begin(), myvector.end());
                // update the threshold for short peaks
                d_ShThres = 0.7*d_ShThres +0.3*0.9*(myvector[Peak2Pick]);
            }
            UpdateCounter++;
            int tempLgThres;
            if ((UpdateCounter % d_UpdatePeriod) - d_LgSeqLen == 0){
                if(LgPeakRxd > 0){
                    tempLgThres = LgPeakRxd;
                }
                else{
                    tempLgThres = MovAvgData[i]*d_LgSeqLen/3.4641; //sqrt(12)=3.4641
                    d_ShThres = 0.7*d_ShThres +0.3*1;
                }
                d_LgThres = 0.7*d_LgThres +0.3*0.8*tempLgThres;
                LgPeakRxd = 0;
            }
            if (UpdateCounter == d_UpdatePeriod)
                UpdateCounter = 0;
            pmt::pmt_t msg_sh = pmt::from_float(d_ShThres);
            pmt::pmt_t msg_lg = pmt::from_float(d_LgThres);
            //std::cout << d_ShThres << ":" << d_LgThres << ":" << LgPeakRxd <<std::endl;

            message_port_pub(pmt::mp("out_sh"), msg_sh);
            message_port_pub(pmt::mp("out_lg"), msg_lg);
            shth[i-history()] = d_ShThres;
            lgth[i-history()] = d_LgThres;
        }

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace ncofdm */
} /* namespace gr */

