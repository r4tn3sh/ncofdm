# ncofdm v6.7
Example codes are ready for bulk data collection.

###ncofdm v6.6
Corrected a bug in logcorrV2. Made corresponding adjustment elsewhere.

###ncofdm v6.5
Examples have been added where python file can read the configuration file sent from remote computer. This method should be useful for multiple experiment.

###ncofdm V6.4
In the example folder both tx and rx codes have been modified to streamline the configuration in the future.

###ncofdm V6.3
This version has better loopback example, but has not been tested with USRPs (it should work). contains stream2fftvector and stream_to_fftstream. File names in file sinks have been generalizedi only in loopback example.
Going forward we still have to complete NC-OFDM full chain. After FFT at the receiver there is complete amplitude match but phase is way off (need pilots?).

###ncofdm V6.2
Version 6.2 has GNURadio companion examples in the folder. 'ncofdm_loopback.grc'is the ongoing effort on making a complete nc-ofdm chain. We have yet to decode the OFDM signal after finding the FFT boundry. 

###ncofdm v6.1
Version 6.1 is built on top of version 6. Version 6 had a long correlator with threshold adjustment. This version modifies the short correlator to allow threshold adjustment in the block itself by using average value of short corr.
