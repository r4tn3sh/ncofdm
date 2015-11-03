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

#ifndef INCLUDED_NCOFDM_ADD_CP_SYNC_IMPL_H
#define INCLUDED_NCOFDM_ADD_CP_SYNC_IMPL_H

#include <ncofdm/add_cp_sync.h>

namespace gr {
    namespace ncofdm {

        class add_cp_sync_impl : public add_cp_sync
        {
            private:
                size_t d_fft_len;
                //! FFT length + CP length in samples
                size_t d_output_size;
                //! Length of the cyclic prefix in samples
                int d_cp_len;
                int d_data_len;
                float d_sp_ratio_db;
                int d_shseq_len;
                int d_shseq_rep;
                int d_lgseq_len;
                std::vector<gr_complex> d_shseq;
                std::vector<gr_complex> d_lgseq;
            protected:
                int calculate_output_stream_length(const gr_vector_int &ninput_items);

            public:
                add_cp_sync_impl(
                        int fft_len, 
                        int cp_len, 
                        float sp_ratio_db, 
                        int data_len,
                        int shseq_len, 
                        int shseq_rep, 
                        const std::vector<gr_complex> &shseq, 
                        int lgseq_len, 
                        const std::vector<gr_complex> &lgseq, 
                        const std::string &len_tag_key
                        );
                ~add_cp_sync_impl();

                // Where all the action really happens
                int work(int noutput_items,
                        gr_vector_int &ninput_items,
                        gr_vector_const_void_star &input_items,
                        gr_vector_void_star &output_items);
        };

    } // namespace ncofdm
} // namespace gr

#endif /* INCLUDED_NCOFDM_ADD_CP_SYNC_IMPL_H */

