#!/usr/bin/env python2
# coding: utf8

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from gnuradio import analog

from math import cos,sin

import grphasecomparator, cmath, os, time

class qa_root_sync(gr_unittest.TestCase):
    two_pi = cmath.pi * 2

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def _get_output(self, samp_rate=430, freq0=43, freq1=43, delay0=0, delay1=0):
        ##################################################
        # Blocks
        ##################################################
        sig0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, freq0, 1, 0)
        sig1 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, freq1, 1, 0)
        d0   = blocks.delay(gr.sizeof_gr_complex*1, delay0)
        d1   = blocks.delay(gr.sizeof_gr_complex*1, delay1)
        pc   = grphasecomparator.phase_comparator()
        fin  = blocks.head(gr.sizeof_float*1, 100);
        dst  = blocks.vector_sink_f()

        ##################################################
        # Connections
        ##################################################
        self.tb.connect((d1,   0), (pc,  1))
        self.tb.connect((d0,   0), (pc,  0))
        self.tb.connect((sig1, 0), (d1,  0))
        self.tb.connect((sig0, 0), (d0,  0))
        self.tb.connect((pc,   0), (fin, 0))
        self.tb.connect((fin,  0), (dst, 0))

        ##################################################
        # Run
        ##################################################
        self.tb.run()

        return dst.data()

    def test_001(self):
        output = self._get_output(delay0=0, delay1=0)
        for s in output:
            self.assertAlmostEqual(s, 0, delta=0.0001);

if __name__ == '__main__':
    x = os.getenv("TEST_PREFIX")

    if not x:
        x = "test"

    gr_unittest.TestLoader.testMethodPrefix = x
    gr_unittest.main ()
