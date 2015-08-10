/* -*- c++ -*- */
/* 
 * Copyright 2015 Paul Miller <paul@voltar.org>
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
#include "phase_comparator_impl.h"

namespace gr { namespace phase_comparator {

phase_comparator::sptr phase_comparator::make() {
    return gnuradio::get_initial_sptr (new phase_comparator_impl());
}

phase_comparator_impl::phase_comparator_impl() : gr::sync_block("phase_comparator",
    gr::io_signature::make(2, 2, sizeof(gr_complex)), gr::io_signature::make(1, 1, sizeof(float))) { }

phase_comparator_impl::~phase_comparator_impl() { }

int phase_comparator_impl::work(int noutput_items, gr_vector_const_void_star &input_items,
          gr_vector_void_star &output_items) {

    const gr_complex *lhs = (const gr_complex *) input_items[0];
    const gr_complex *rhs = (const gr_complex *) input_items[1];

    float *out = (float *) output_items[0];

    fprintf(stderr, "noutput_items = %d\n", noutput_items);

    return noutput_items;
}

} /* namespace phase_comparator */ } /* namespace gr */

