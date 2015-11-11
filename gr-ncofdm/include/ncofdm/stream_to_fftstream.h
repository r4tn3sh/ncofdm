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


#ifndef INCLUDED_NCOFDM_STREAM_TO_FFTSTREAM_H
#define INCLUDED_NCOFDM_STREAM_TO_FFTSTREAM_H

#include <ncofdm/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace ncofdm {

    /*!
     * \brief <+description of block+>
     * \ingroup ncofdm
     *
     */
    class NCOFDM_API stream_to_fftstream : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<stream_to_fftstream> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of ncofdm::stream_to_fftstream.
       *
       * To avoid accidental use of raw pointers, ncofdm::stream_to_fftstream's
       * constructor is in a private implementation
       * class. ncofdm::stream_to_fftstream::make is the public interface for
       * creating new instances.
       */
      static sptr make(int fft_len, int cp_len);
    };

  } // namespace ncofdm
} // namespace gr

#endif /* INCLUDED_NCOFDM_STREAM_TO_FFTSTREAM_H */

