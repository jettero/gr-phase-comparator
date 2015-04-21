#!/usr/bin/env python2
# coding: utf8

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from math import cos,sin

import grphasecomparator, cmath, os

class qa_root_sync(gr_unittest.TestCase):
    two_pi = cmath.pi * 2

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def _build_inputs(self, time=1, freq=1, samp_rate=43, phase1=0, phase2=0):
        self.signal0 = []
        self.signal1 = []

        omega = 2 * cmath.pi * freq

        for i in range(time * samp_rate):
            t = i / samp_rate
            self.signal0.append( cos(omega*t + phase1) + sin(omega*t + phase1)*1j )
            self.signal1.append( cos(omega*t + phase2) + sin(omega*t + phase2)*1j )

    def _do_test(self, time=1, freq=1, samp_rate=43, phase1=0, phase2=0):
        pc = grphasecomparator.phase_comparator()
        self._build_inputs()

        sig0 = blocks.vector_source_c(self.signal0, False)
        sig1 = blocks.vector_source_c(self.signal1, False)
        dst  = blocks.vector_sink_c()

        self.tb.connect(sig0, (pc,0))
        self.tb.connect(sig1, (pc,1))
        self.tb.connect(pc, dst)
        self.tb.run()

        dphase_ar = dst.data()
        for s in dphase_ar:
            self.assertAlmostEqual(s, 0, delta=0.0001);

# XXX: ../../../cs/cs700.1/c/python/qa_root_sync.py

    def test_001_zero_offset(self):
        self._do_test(phase1=0, phase2=0)

if __name__ == '__main__':
    x = os.getenv("TEST_PREFIX")

    if not x:
        x = "test"

    gr_unittest.TestLoader.testMethodPrefix = x
    gr_unittest.main ()
