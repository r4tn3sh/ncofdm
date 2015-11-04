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


#ifndef INCLUDED_NCOFDM_LONGPNCORRV2_H
#define INCLUDED_NCOFDM_LONGPNCORRV2_H

#include <ncofdm/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace ncofdm {

    /*!
     * \brief <+description of block+>
     * \ingroup ncofdm
     *
     */
    class NCOFDM_API LongPNcorrV2 : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<LongPNcorrV2> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of ncofdm::LongPNcorrV2.
       *
       * To avoid accidental use of raw pointers, ncofdm::LongPNcorrV2's
       * constructor is in a private implementation
       * class. ncofdm::LongPNcorrV2::make is the public interface for
       * creating new instances.
       */
      static sptr make(int fft_len, int cp_len, int LgSeqLen, const std::vector<gr_complex> &LgSeq, float LgThres, int UpdateInterval);
    };

  } // namespace ncofdm
} // namespace gr

#endif /* INCLUDED_NCOFDM_LONGPNCORRV2_H */

