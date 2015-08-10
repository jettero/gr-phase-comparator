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


#ifndef INCLUDED_PHASE_COMPARATOR_PHASE_COMPARATOR_H
#define INCLUDED_PHASE_COMPARATOR_PHASE_COMPARATOR_H

#include <phase_comparator/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace phase_comparator {

    /*!
     * \brief <+description of block+>
     * \ingroup phase_comparator
     *
     */
    class PHASE_COMPARATOR_API phase_comparator : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<phase_comparator> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of phase_comparator::phase_comparator.
       *
       * To avoid accidental use of raw pointers, phase_comparator::phase_comparator's
       * constructor is in a private implementation
       * class. phase_comparator::phase_comparator::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace phase_comparator
} // namespace gr

#endif /* INCLUDED_PHASE_COMPARATOR_PHASE_COMPARATOR_H */

