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

#ifndef INCLUDED_NCOFDM_UNDERLAY_SYNC_DETECTOR_IMPL_H
#define INCLUDED_NCOFDM_UNDERLAY_SYNC_DETECTOR_IMPL_H

#include <ncofdm/underlay_sync_detector.h>
#include <gnuradio/filter/fft_filter.h>

namespace gr {
    namespace ncofdm {

        class underlay_sync_detector_impl : public underlay_sync_detector
        {
            private:
                size_t d_fft_len;
                //! FFT length + CP length in samples
                size_t d_output_size;
                //! Length of the cyclic prefix in samples
                int d_cp_size;
                int d_sync_len;
                std::vector<gr_complex> d_symbols;
                filter::kernel::fft_filter_ccc  *d_filter;

            public:
                underlay_sync_detector_impl(size_t input_size, size_t output_size, int sync_len, const std::vector<gr_complex> &symbols);
                ~underlay_sync_detector_impl();

                //std::vector<gr_complex> symbols() const;
                void set_symbols(const std::vector<gr_complex> &symbols);

                // Where all the action really happens
                int work(int noutput_items,
                        gr_vector_const_void_star &input_items,
                        gr_vector_void_star &output_items);
        };

    } // namespace ncofdm
} // namespace gr

#endif /* INCLUDED_NCOFDM_UNDERLAY_SYNC_DETECTOR_IMPL_H */

