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


#ifndef INCLUDED_NCOFDM_UNDERLAY_SYNC_CP_H
#define INCLUDED_NCOFDM_UNDERLAY_SYNC_CP_H

#include <ncofdm/api.h>
#include <gnuradio/tagged_stream_block.h>

namespace gr {
  namespace ncofdm {

    /*!
     * \brief <+description of block+>
     * \ingroup ncofdm
     *
     */
    class NCOFDM_API underlay_sync_cp : virtual public gr::tagged_stream_block
    {
     public:
      typedef boost::shared_ptr<underlay_sync_cp> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of ncofdm::underlay_sync_cp.
       *
       * To avoid accidental use of raw pointers, ncofdm::underlay_sync_cp's
       * constructor is in a private implementation
       * class. ncofdm::underlay_sync_cp::make is the public interface for
       * creating new instances.
       */
      static sptr make(size_t input_size, size_t output_size, int rolloff_len, int sync_len, const std::string &len_tag_key, const std::vector<gr_complex> &symbols);
    };

  } // namespace ncofdm
} // namespace gr

#endif /* INCLUDED_NCOFDM_UNDERLAY_SYNC_CP_H */

