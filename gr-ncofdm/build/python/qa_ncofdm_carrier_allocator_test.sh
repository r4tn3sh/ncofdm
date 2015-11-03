#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/root/gr-ncofdm/python
export PATH=/root/gr-ncofdm/build/python:$PATH
export LD_LIBRARY_PATH=/root/gr-ncofdm/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/root/gr-ncofdm/build/swig:$PYTHONPATH
/usr/bin/python2 /root/gr-ncofdm/python/qa_ncofdm_carrier_allocator.py 
