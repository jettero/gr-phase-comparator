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

#ifndef INCLUDED_PHASE_COMPARATOR_PHASE_COMPARATOR_IMPL_H
#define INCLUDED_PHASE_COMPARATOR_PHASE_COMPARATOR_IMPL_H

#include <phase_comparator/phase_comparator.h>
#include <gnuradio/blocks/multiply_conjugate_cc.h>
#include <gnuradio/blocks/complex_to_arg.h>

namespace gr { namespace phase_comparator {

class phase_comparator_impl : public phase_comparator {
    private:
        gr::blocks::multiply_conjugate_cc::sptr conj;
        gr::blocks::complex_to_arg::sptr arg;

    public:
        phase_comparator_impl();
        ~phase_comparator_impl();

        // Where all the action really happens
        int work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items);
};

} /* namespace phase_comparator */ } /* namespace gr */

#endif /* INCLUDED_PHASE_COMPARATOR_PHASE_COMPARATOR_IMPL_H */

