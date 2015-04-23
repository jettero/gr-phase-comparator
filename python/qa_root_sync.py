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

    def _get_output(self, outputs=860, samp_rate=860, freq0=43, freq1=43, delay0=0, delay1=0):
        ##################################################
        # Blocks
        ##################################################
        sig0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, freq0, 1, 0)
        sig1 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, freq1, 1, 0)
        d0   = blocks.delay(gr.sizeof_gr_complex*1, delay0)
        d1   = blocks.delay(gr.sizeof_gr_complex*1, delay1)
        pc   = grphasecomparator.phase_comparator()
        fin  = blocks.head(gr.sizeof_float*1, outputs)
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

    def test_000(self):
        output = self._get_output(delay0=0, delay1=0)
        for s in output:
            self.assertAlmostEqual(s, 0, delta=0.0001)

    def test_001(self):
        output = self._get_output(delay0=0, delay1=25)[25:]

       #print ""
       #for (i, s1) in enumerate(output):
       #    j = (i+1) % len(output)
       #    s2 = output[j]
       #    print "[%3d,%3d %%4.1fv%4.1f]" % (i,j, s1, s2),
       #    if ( j % 3 ) == 0:
       #        print ""
       #print ""

        for (i, s1) in enumerate(output):
            s2 = output[ (i+1) % len(output) ]
            self.assertAlmostEqual(s1, s2, delta=0.0001)

   #def test_002(self):
   #    output = self._get_output(delay0=25, delay1=0)[25:]
   #    for (i, s1) in enumerate(output):
   #        s2 = output[ (i+1) % len(output) ]
   #        self.assertAlmostEqual(s1, s2, delta=0.0001)

   #def test_003(self):
   #    output = self._get_output(delay0=0, delay1=100)[100:]
   #    for (i, s1) in enumerate(output):
   #        s2 = output[ (i+1) % len(output) ]
   #        self.assertAlmostEqual(s1, s2, delta=0.0001)

   #def test_004(self):
   #    output = self._get_output(delay0=100, delay1=0)[100:]
   #    for (i, s1) in enumerate(output):
   #        s2 = output[ (i+1) % len(output) ]
   #        self.assertAlmostEqual(s1, s2, delta=0.0001)

   #def test_005(self):
   #    output = self._get_output(freq0=43, freq1=47, delay0=100, delay1=100)[100:]

   #    for (i,s1) in enumerate(output):
   #        for (j,s2) in enumerate(output[i:]):
   #            for s3 in output[j:]:
   #                self.assertAlmostEqual( (s2-s1), (s3-s2), delta=0.01)

if __name__ == '__main__':
    x = os.getenv("TEST_PREFIX")

    if not x:
        x = "test"

    gr_unittest.TestLoader.testMethodPrefix = x
    gr_unittest.main ()
