
from gnuradio import gr
from operator import itemgetter

import numpy, math, cmath

# XXX: tempoary
import sys,os

INDEX_MODE  = 1234
MINMAX_MODE = 5678

TWO_PI = 2 * math.pi

class phase_comparator(gr.sync_block):
    """
    Compare the difference in phase between two complex signals (accounting for wrapping)
    """

    def __init__(self, counter_limit=5):
        """
        Create the block block

        Args:
        counter_limit = max_size of counter before rollover
        """

        self._c = 0
        self._counter_limit = counter_limit

        if os.getenv("PHC_DEBUG"):
            self._debug = True
        else:
            self._debug = False

        gr.sync_block.__init__(self, "phase_comparator", ["complex64","complex64"], ["float32"])

    def work(self, input_items, output_items):
        for i in range( len(input_items[0]) ):
            x = input_items[0][i]
            y = input_items[1][i]

            px = cmath.phase(x)
            py = cmath.phase(y)
            dp = px - py

            if self._debug:
                os.write(2, "%6.2f - %6.2f = %6.2f" % (px,py,dp) )

            if dp > math.pi:
                dp = dp - TWO_PI

            if dp < -math.pi:
                dp = dp + TWO_PI

            if self._debug:
                os.write(2, " [corrected] %6.2f\n" % dp)

            output_items[0][i] = dp

        return len(input_items[0])
