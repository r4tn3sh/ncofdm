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

#ifndef INCLUDED_NCOFDM_NCOFDM_CARRIER_ALLOCATOR_IMPL_H
#define INCLUDED_NCOFDM_NCOFDM_CARRIER_ALLOCATOR_IMPL_H

#include <ncofdm/ncofdm_carrier_allocator.h>

namespace gr {
    namespace ncofdm {

        class ncofdm_carrier_allocator_impl : public ncofdm_carrier_allocator
        {
            private:
                //! FFT length
                const int d_fft_len;
                //! Which carriers/symbols carry data
                std::vector<std::vector<int> > d_occupied_carriers;
                //! Which carriers/symbols carry pilots symbols
                std::vector<std::vector<int> > d_pilot_carriers;
                //! Value of said pilot symbols
                const std::vector<std::vector<gr_complex> > d_pilot_symbols;
                int d_symbols_per_set;

            protected:
                int calculate_output_stream_length(const gr_vector_int &ninput_items);

            public:
                ncofdm_carrier_allocator_impl(
                        int fft_len,
                        const std::vector<std::vector<int> > &occupied_carriers,
                        const std::vector<std::vector<int> > &pilot_carriers,
                        const std::vector<std::vector<gr_complex> > &pilot_symbols,
                        const std::string &len_tag_key
                        );
                ~ncofdm_carrier_allocator_impl();

                std::string len_tag_key() { return d_length_tag_key_str; };

                const int fft_len() { return d_fft_len; };
                std::vector<std::vector<int> > occupied_carriers() { return d_occupied_carriers; };

                // Where all the action really happens
                int work(int noutput_items,
                        gr_vector_int &ninput_items,
                        gr_vector_const_void_star &input_items,
                        gr_vector_void_star &output_items);
        };

    } // namespace ncofdm
} // namespace gr

#endif /* INCLUDED_NCOFDM_NCOFDM_CARRIER_ALLOCATOR_IMPL_H */

