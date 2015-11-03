/* -*- c++ -*- */

#define NCOFDM_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "ncofdm_swig_doc.i"

%{
#include "ncofdm/ncofdm_carrier_allocator.h"
#include "ncofdm/add_cp_sync.h"
#include "ncofdm/ShortPNcorr.h"
#include "ncofdm/stream2fftvector.h"
#include "ncofdm/LongPNcorr.h"
#include "ncofdm/FreqOffCalc.h"
#include "ncofdm/DyThresAdjust.h"
#include "ncofdm/ShortPNdetector.h"
#include "ncofdm/ncofdm_carrier_allocator.h"
#include "ncofdm/add_cp_sync.h"
#include "ncofdm/ShortPNcorr.h"
#include "ncofdm/stream2fftvector.h"
#include "ncofdm/LongPNcorr.h"
#include "ncofdm/FreqOffCalc.h"
#include "ncofdm/DyThresAdjust.h"
#include "ncofdm/ShortPNdetector.h"
%}


%include "ncofdm/ncofdm_carrier_allocator.h"
GR_SWIG_BLOCK_MAGIC2(ncofdm, ncofdm_carrier_allocator);
%include "ncofdm/add_cp_sync.h"
GR_SWIG_BLOCK_MAGIC2(ncofdm, add_cp_sync);
%include "ncofdm/ShortPNcorr.h"
GR_SWIG_BLOCK_MAGIC2(ncofdm, ShortPNcorr);

%include "ncofdm/stream2fftvector.h"
GR_SWIG_BLOCK_MAGIC2(ncofdm, stream2fftvector);

%include "ncofdm/LongPNcorr.h"
GR_SWIG_BLOCK_MAGIC2(ncofdm, LongPNcorr);
%include "ncofdm/FreqOffCalc.h"
GR_SWIG_BLOCK_MAGIC2(ncofdm, FreqOffCalc);

%include "ncofdm/DyThresAdjust.h"
GR_SWIG_BLOCK_MAGIC2(ncofdm, DyThresAdjust);
%include "ncofdm/ShortPNdetector.h"
GR_SWIG_BLOCK_MAGIC2(ncofdm, ShortPNdetector);
