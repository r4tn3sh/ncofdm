# ncofdm v8.3
updated "packet_len=len(occupied_carriers[0])" in examples
### ncofdm v8.2
pnseq_offset was changed in const_tx_general.py
### ncofdm v8.1
usrp_gain is added
### ncofdm v8
Better control of power ratio is available. The "add_cp_underlay" block now receives the input with unit power over complete bandwidth (if only a subset of carriers are used then power is calculated accordingly). The underlay amplitude is kept at 0.1 and based on signal-to-underlay ratio overlay signal is adjusted. More than 20dB signal-to-underlay is not allowed, since input to USRP sink needs to be within unit circle in complex plane. Before feeding the signal to USRP sink a constant "final_gain" is multiplied which ensures that underlay power is same as noise.
