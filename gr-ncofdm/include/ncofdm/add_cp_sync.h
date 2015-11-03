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


#ifndef INCLUDED_NCOFDM_ADD_CP_SYNC_H
#define INCLUDED_NCOFDM_ADD_CP_SYNC_H

#include <ncofdm/api.h>
#include <gnuradio/tagged_stream_block.h>

namespace gr {
  namespace ncofdm {

    /*!
     * \brief <+description of block+>
     * \ingroup ncofdm
     *
     */
    class NCOFDM_API add_cp_sync : virtual public gr::tagged_stream_block
    {
     public:
      typedef boost::shared_ptr<add_cp_sync> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of ncofdm::add_cp_sync.
       *
       * To avoid accidental use of raw pointers, ncofdm::add_cp_sync's
       * constructor is in a private implementation
       * class. ncofdm::add_cp_sync::make is the public interface for
       * creating new instances.
       */
      static sptr make(
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
    };

  } // namespace ncofdm
} // namespace gr

#endif /* INCLUDED_NCOFDM_ADD_CP_SYNC_H */

