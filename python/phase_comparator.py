
import numpy, cmath
from gnuradio import gr
from operator import itemgetter

INDEX_MODE  = 1234
MINMAX_MODE = 5678

class phase_comparator(gr.sync_block):
    """
    Compare the difference in phase between two complex signals (accounting for wrapping)
    """

    def __init__(self):
        """
        Create the block block

        Args:
        """

        gr.sync_block.__init__(self, "phase_comparator", ["complex64","complex64"], ["float32"])

    def work(self, input_items, output_items):
        for i in range( len(input_items[0]) ):
            x = input_items[0][i]
            y = input_items[1][i]

            output_items[0][i] = cmath.phase(x) - cmath.phase(y)

        return len(input_items[0])
