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
#include "add_cp_sync_impl.h"

int seqcnt = 0;
namespace gr {
    namespace ncofdm {

        add_cp_sync::sptr
            add_cp_sync::make(
                    int     fft_len, 
                    int     cp_len, 
                    float   sp_ratio_db, 
                    int     data_len,
                    int     shseq_len, 
                    int     shseq_rep, 
                    const   std::vector<gr_complex> &shseq, 
                    int     lgseq_len, 
                    const   std::vector<gr_complex> &lgseq, 
                    const   std::string &len_tag_key
                    )
            {
                return gnuradio::get_initial_sptr
                    (new add_cp_sync_impl(fft_len, cp_len, sp_ratio_db, data_len, shseq_len, shseq_rep, shseq, lgseq_len, lgseq, len_tag_key));
            }

        /*
         * The private constructor
         */
        add_cp_sync_impl::add_cp_sync_impl(
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
                )
            : gr::tagged_stream_block("add_cp_sync",
                    gr::io_signature::make(1, 1, fft_len*sizeof(gr_complex)),
                    gr::io_signature::make(1, 1, sizeof(gr_complex)), len_tag_key),
            d_fft_len(fft_len),
            d_cp_len(cp_len),
            d_output_size(cp_len+fft_len),
            d_sp_ratio_db(sp_ratio_db),
            d_data_len(data_len),
            d_shseq_len(shseq_len),
            d_shseq_rep(shseq_rep),
            d_shseq(shseq),
            d_lgseq_len(lgseq_len),
            d_lgseq(lgseq)        
        {
            //start sanity check
            if ((d_shseq_len*d_shseq_rep + d_lgseq_len) % (d_output_size)){
                throw std::invalid_argument("Undelay PN sequence boundry should match with OFDM boundry");
            }

            if ((d_data_len) % (d_output_size)){
                throw std::invalid_argument("Data boundry should match with OFDM boundry");
            }
            //set variables
            set_relative_rate(d_output_size);
            if (len_tag_key.empty()) {
                set_output_multiple(d_output_size);
            } else {
                set_tag_propagation_policy(TPP_DONT);
            }        
        }

        /*
         * Our virtual destructor.
         */
        add_cp_sync_impl::~add_cp_sync_impl()
        {
        }

        int
            add_cp_sync_impl::calculate_output_stream_length(const gr_vector_int &ninput_items)
            {
                int noutput_items = ninput_items[0] * d_output_size;
                return noutput_items ;
            }

        int
            add_cp_sync_impl::work (int noutput_items,
                    gr_vector_int &ninput_items,
                    gr_vector_const_void_star &input_items,
                    gr_vector_void_star &output_items)
            {
                gr_complex *in = (gr_complex *) input_items[0];
                gr_complex *out = (gr_complex *) output_items[0];
                // Do <+signal processing+>
                float sp_ratio = sqrt(pow(10,d_sp_ratio_db/10));
                int symbols_to_read = 0;
                symbols_to_read = std::min(noutput_items / (int) d_output_size, ninput_items[0]);
                noutput_items = symbols_to_read * d_output_size;

                for (int sym_idx = 0; sym_idx < symbols_to_read; sym_idx++) {
                    memcpy((void *)(out + d_cp_len), (void *) in, d_fft_len * sizeof(gr_complex));
                    memcpy((void *) out, (void *) (in + d_fft_len - d_cp_len), d_cp_len * sizeof(gr_complex));
                    //******add the underlay sync signal******
                    for (int i = 0; i < d_output_size; i++) {
                        if (seqcnt == d_shseq_rep*d_shseq_len+d_lgseq_len+d_data_len)
                            seqcnt = 0;
                        //out[i] = out[i] + ((gr_complex)(0.316)*d_symbols[seqcnt++]);
                        if (seqcnt < d_shseq_rep*d_shseq_len){
                            out[i] = out[i] + ((gr_complex)(1/sp_ratio)*d_shseq[seqcnt%d_shseq_len]);
                        }
                        else if (seqcnt < d_shseq_rep*d_shseq_len+d_lgseq_len){
                            out[i] = out[i] + ((gr_complex)(1/sp_ratio)*d_lgseq[seqcnt - d_shseq_rep*       d_shseq_len]);
                        }
                        seqcnt++;
                    }
                    in += d_fft_len;
                    out += d_output_size;
                }

                // Tell runtime system how many output items we produced.
                return noutput_items;        
            }

    } /* namespace ncofdm */
} /* namespace gr */

