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
#include "underlay_sync_cp_impl.h"

int seqcnt = 0;
namespace gr {
    namespace ncofdm {

        underlay_sync_cp::sptr
            underlay_sync_cp::make(size_t input_size, size_t output_size, int rolloff_len, int sync_len, const std::string &len_tag_key, const std::vector<gr_complex> &symbols)
            {
                return gnuradio::get_initial_sptr
                    (new underlay_sync_cp_impl(input_size, output_size, rolloff_len, sync_len, len_tag_key, symbols));
            }

        /*
         * The private constructor
         */
        underlay_sync_cp_impl::underlay_sync_cp_impl(size_t input_size, size_t output_size, int rolloff_len, int sync_len, const std::string &len_tag_key, const std::vector<gr_complex> &symbols)
            : gr::tagged_stream_block("underlay_sync_cp",
                    gr::io_signature::make(1, 1, input_size*sizeof(gr_complex)),
                    gr::io_signature::make(1, 1, sizeof(gr_complex)), 
                    len_tag_key),
            d_fft_len(input_size),
            d_output_size(output_size),
            d_cp_size(output_size - input_size),
            d_rolloff_len(rolloff_len),
            d_sync_len(sync_len),
            d_symbols(symbols),
            d_up_flank((rolloff_len ? rolloff_len-1 : 0), 0),
            d_down_flank((rolloff_len ? rolloff_len-1 : 0), 0),
            d_delay_line(0, 0)
        {
		if (d_symbols.size() < d_sync_len*d_output_size) {
		  throw std::invalid_argument("sync symbols must be more than intended sync size");
		}
                set_relative_rate(d_output_size);

                // Flank of length 1 would just be rectangular
                if (d_rolloff_len == 1) {
                    d_rolloff_len = 0;
                }
                if (d_rolloff_len) {
                    d_delay_line.resize(d_rolloff_len-1, 0);
                    if (rolloff_len > d_cp_size) {
                        throw std::invalid_argument("cyclic prefixer: rolloff len must smaller than the cyclic prefix.");
                    }
                    // The actual flanks are one sample shorter than d_rolloff_len, because the
                    // first sample of the up- and down flank is always zero and one, respectively
                    for (int i = 1; i < d_rolloff_len; i++) {
                        d_up_flank[i-1]   = 0.5 * (1 + cos(M_PI * i/rolloff_len - M_PI));
                        d_down_flank[i-1] = 0.5 * (1 + cos(M_PI * (rolloff_len-i)/rolloff_len - M_PI));
                    }
                }

                if (len_tag_key.empty()) {
                    set_output_multiple(d_output_size);
                } else {
                    set_tag_propagation_policy(TPP_DONT);
                }
        }

        /*
         * Our virtual destructor.
         */
        underlay_sync_cp_impl::~underlay_sync_cp_impl()
        {
        }

        int
            underlay_sync_cp_impl::calculate_output_stream_length(const gr_vector_int &ninput_items)
            {
                int nout = ninput_items[0] * d_output_size + d_delay_line.size();
                return nout;
            }

        int
            underlay_sync_cp_impl::work (int noutput_items,
                    gr_vector_int &ninput_items,
                    gr_vector_const_void_star &input_items,
                    gr_vector_void_star &output_items)
            {
                gr_complex *in = (gr_complex *) input_items[0];
                gr_complex *out = (gr_complex *) output_items[0];
                int symbols_to_read = 0;

                // 1) Figure out if we're in freewheeling or packet mode
                if (!d_length_tag_key_str.empty()) {
                    symbols_to_read = ninput_items[0];
                    noutput_items = symbols_to_read * d_output_size + d_delay_line.size();
                } else {
                    symbols_to_read = std::min(noutput_items / (int) d_output_size, ninput_items[0]);
                    noutput_items = symbols_to_read * d_output_size;
                }

                // 2) Do the cyclic prefixing and, optionally, the pulse shaping
                for (int sym_idx = 0; sym_idx < symbols_to_read; sym_idx++) {
                    memcpy((void *)(out + d_cp_size), (void *) in, d_fft_len * sizeof(gr_complex));
                    memcpy((void *) out, (void *) (in + d_fft_len - d_cp_size), d_cp_size * sizeof(gr_complex));
                    //******add the underlay sync signal******
                    for (int i = 0; i < d_output_size; i++) {
                        if (seqcnt == d_sync_len*d_output_size) //###### CAREFUL: not checking limit
                            seqcnt = 0;
                        //out[i] = out[i] + ((gr_complex)(0.316)*d_symbols[seqcnt++]);
                        out[i] = out[i] + ((gr_complex)(0.316)*d_symbols[seqcnt++]);
                    }
                    if (d_rolloff_len) {
                        for (int i = 0; i < d_rolloff_len-1; i++) {
                            out[i] = out[i] * d_up_flank[i] + d_delay_line[i];
                            d_delay_line[i] = in[i] * d_down_flank[i];
                        }
                    }
                    in += d_fft_len;
                    out += d_output_size;
                }

                // 3) If we're in packet mode:
                //    - flush the delay line, if applicable
                //    - Propagate tags
                if (!d_length_tag_key_str.empty()) {
                    if (d_rolloff_len) {
                        for (unsigned i = 0; i < d_delay_line.size(); i++) {
                            *out++ = d_delay_line[i];
                        }
                        d_delay_line.assign(d_delay_line.size(), 0);
                    }
                    std::vector<tag_t> tags;
                    get_tags_in_range(
                            tags, 0,
                            nitems_read(0), nitems_read(0)+symbols_to_read
                            );
                    for (unsigned i = 0; i < tags.size(); i++) {
                        tags[i].offset = ((tags[i].offset - nitems_read(0)) * d_output_size) + nitems_written(0);
                        add_item_tag(0,
                                tags[i].offset,
                                tags[i].key,
                                tags[i].value
                                );
                    }
                } else {
                    consume_each(symbols_to_read);
                }

                return noutput_items;
            }

    } /* namespace ncofdm */
} /* namespace gr */


