#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/root/gr-ncofdm/lib
export PATH=/root/gr-ncofdm/build/lib:$PATH
export LD_LIBRARY_PATH=/root/gr-ncofdm/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-ncofdm 
