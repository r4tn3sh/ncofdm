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

#ifndef INCLUDED_NCOFDM_SHORTPNCORR_IMPL_H
#define INCLUDED_NCOFDM_SHORTPNCORR_IMPL_H

#include <ncofdm/ShortPNcorr.h>
#include <gnuradio/filter/fft_filter.h>

namespace gr {
    namespace ncofdm {

        class ShortPNcorr_impl : public ShortPNcorr
        {
            private:
                int d_fft_len;
                int d_cp_len;
                int d_ShSeqRep;
                int d_ShSeqLen; 
                std::vector<gr_complex> d_ShSeq;
                std::vector<gr_complex> d_symbols;
                filter::kernel::fft_filter_ccc  *d_filter;
                filter::kernel::fft_filter_ccc  *d_Shfilter;

            public:
                ShortPNcorr_impl(int fft_len, int cp_len, int ShSeqRep, int ShSeqLen, const std::vector<gr_complex> &ShSeq);
                ~ShortPNcorr_impl();

                // Where all the action really happens
                int work(int noutput_items,
                        gr_vector_const_void_star &input_items,
                        gr_vector_void_star &output_items);
        };

    } // namespace ncofdm
} // namespace gr

#endif /* INCLUDED_NCOFDM_SHORTPNCORR_IMPL_H */

