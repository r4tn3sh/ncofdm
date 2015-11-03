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
#include "ShortPNcorr_impl.h"
#include <volk/volk.h>


namespace gr {
    namespace ncofdm {

        ShortPNcorr::sptr
            ShortPNcorr::make(
                    int fft_len, 
                    int cp_len, 
                    int ShSeqRep, 
                    int ShSeqLen, 
                    const std::vector<gr_complex> &ShSeq
                    )
            {
                return gnuradio::get_initial_sptr
                    (new ShortPNcorr_impl(fft_len, cp_len, ShSeqRep, ShSeqLen, ShSeq));
            }

        /*
         * The private constructor
         */
        ShortPNcorr_impl::ShortPNcorr_impl(
                int fft_len, 
                int cp_len, 
                int ShSeqRep, 
                int ShSeqLen, 
                const std::vector<gr_complex> &ShSeq
                )
            : gr::sync_block("ShortPNcorr",
                    gr::io_signature::make(1, 1, sizeof(gr_complex)),
                    gr::io_signature::make(2, 2, sizeof(gr_complex))),
                    //gr::io_signature::make(1, 1, sizeof(gr_complex))),
                    //gr::io_signature::make3(3, 3, sizeof(gr_complex), sizeof(gr_complex), sizeof(int))),
                    d_fft_len(fft_len),
                    d_cp_len(cp_len),
                    d_ShSeqRep(ShSeqRep),
                    d_ShSeqLen(ShSeqLen),
                    d_ShSeq(ShSeq)
        {
            //std::reverse(d_ShSeq.begin(), d_ShSeq.end());
            d_Shfilter = new filter::kernel::fft_filter_ccc(1, d_ShSeq);
            set_history(d_ShSeq.size());
            set_output_multiple(2*d_ShSeq.size());            
        }

        /*
         * Our virtual destructor.
         */
        ShortPNcorr_impl::~ShortPNcorr_impl()
        {
        }

        int
            ShortPNcorr_impl::work(int noutput_items,
                    gr_vector_const_void_star &input_items,
                    gr_vector_void_star &output_items)
            {
                const gr_complex *in = (const gr_complex *) input_items[0];
                gr_complex *out = (gr_complex *) output_items[0];
                gr_complex *corr = (gr_complex *) output_items[1];

                memcpy(out, in, sizeof(gr_complex)*noutput_items);

                //d_Shfilter->filter(noutput_items, in, corr);
                for (int i=0; i<noutput_items; i++){
                    corr[i] = 0;
                    for (int j=0; j<d_ShSeqLen; j++){
                        corr[i] = corr[i] + in[i+j]*d_ShSeq[j];
                    }
                }

                // Tell runtime system how many output items we produced.
                return noutput_items;
            }

    } /* namespace ncofdm */
} /* namespace gr */

