#!/bin/bash

# local test (for the debug output)

FAKEROOT=/tmp/$(id -u)/usr

unset NO_INSTALL
export NO_TEST=1 PREFIX=$FAKEROOT

./build.sh

set -x
LD_LIBRARY_PATH=$FAKEROOT/lib \
PYTHONPATH=$FAKEROOT/lib/python2.7/dist-packages/ \
    python python/qa_phase_comparator.py
