
from gnuradio import gr
from gnuradio import blocks

import numpy, math, cmath
import os

DEFAULT_WRAP = [-math.pi*0.9, math.pi*0.9]

class phase_comparator(gr.hier_block2):
    """
    Compare the difference in phase between two complex signals, trying to
    un-wrap PI rolls where possible (i.e., ideally the phase would progress: 3,
    3.1, 3.15, 4, 5, 7, etc)
    """

    def __init__(self, wrap_window=DEFAULT_WRAP):
        """
        The wrapper blockblock handles the arg() rolling

        Args:

            wrap_window: default=%s
                if sample n-1 is above window[1] and sample n is below window[0], then wrap a couple PI

        """ % DEFAULT_WRAP

        self.conj = blocks.multiply_conjugate_cc(1)
        self.arg  = blocks.complex_to_arg(1)
        self.pcw  = _phase_comparator_wrapper(wrap_window)

        # from pydoc:
        # gr.io_signature(int min_streams, int max_streams, int sizeof_stream_item) -> io_signature_sptr

        gr.hier_block2.__init__(self, "phase comparator",
            gr.io_signature(2, 2, gr.sizeof_gr_complex),
            gr.io_signature(1, 1, gr.sizeof_float)
        )

        gr.sizeof_gr_complex

        self.connect( (self,0), (self.conj,0) )
        self.connect( (self,1), (self.conj,1) )
        self.connect( self.conj, self.arg, self.pcw, self )

class _phase_comparator_wrapper(gr.sync_block):

    def __init__(self, wrap_window=DEFAULT_WRAP):
        self._roll = 0
        self._last = 0
        self._rw = wrap_window

        if os.getenv("PHC_DEBUG"):
            self._debug = True
        else:
            self._debug = False

        gr.sync_block.__init__(self, "phase_comparator", ["float32"], ["float32"])

    def work(self, input_items, output_items):
        for (i,v) in enumerate(input_items[0]):
            if self._last >= self._rw[1] and v <= self._rw[0]:
                self._roll = self._roll + 1

            if self._last <= self._rw[0] and v >= self._rw[1]:
                self._roll = self._roll - 1

            output_items[0][i] = v + 2*math.pi*self._roll

            if self._debug:
                os.write(2, "%6.2f,%6.2f [%d] → %0.2f\n" % (self._last,v, self._roll, output_items[0][i]))

            self._last = v

        return len(input_items[0])
