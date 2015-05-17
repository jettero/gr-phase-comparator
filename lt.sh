#!/bin/bash

# local test (for the debug output)

NO_TEST=1 ./build.sh

PHC_DEBUG=1 python python/qa_test.py
