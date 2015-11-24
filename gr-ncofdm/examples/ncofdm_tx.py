#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Transmitter NC-OFDM
# Generated: Tue Nov 24 14:48:29 2015
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import uhd
from gnuradio.digital.utils import tagged_streams
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import ncofdm
import numpy
import random
import sys
import time

from distutils.version import StrictVersion
class ncofdm_tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Transmitter NC-OFDM")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Transmitter NC-OFDM")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ncofdm_tx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.shseq_len = shseq_len = 40
        self.pn_symbols = pn_symbols = (1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, 1, -1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, 1)
        self.occupied_carriers = occupied_carriers = (range(-26, -21)+ range(-20,-7) + range(8, 21) + range(22, 27),)
        self.lgseq_len = lgseq_len = 320
        self.length_tag_name = length_tag_name = "packet_len"
        self.fft_len = fft_len = 64
        self.dataseq_len = dataseq_len = 64
        self.sync_word2 = sync_word2 = (0, 0, 0, 0, 0, 1, 1, -1.0, -1, 1.0, 1, 1.0, -1, -1.0, -1, 1.0, 1, -1.0, 1, 1.0, 1, -1.0, -1, -1.0, -1, 1.0, -1, 1.0, -1, 1.0, 1, -1.0, 0, 1.0, 1, -1.0, 1, 1.0, -1, -1.0, 1, -1.0, -1, -1.0, 1, 1.0, 1, -1.0, 1, 1.0, -1, 1.0, -1, -1.0, -1, 1.0, 1, -1.0, 0, 0, 0, 0, 0, 0)
        self.sync_word1 = sync_word1 = (0, 0, 0, 0, 0, 0, 0, -1.0, 0, 1.0, 0, 1.0, 0, -1.0, 0, 1.0, 0, -1.0, 0, 1.0, 0, -1.0, 0, -1.0, 0, 1.0, 0, 1.0, 0, 1.0, 0, -1.0, 0, 1.0, 0, -1.0, 0, 1.0, 0, -1.0, 0, -1.0, 0, -1.0, 0, 1.0, 0, -1.0, 0, 1.0, 0, 1.0, 0, -1.0, 0, 1.0, 0, -1.0, 0, 0, 0, 0, 0, 0)
        self.sync_len = sync_len = 20
        self.shseq_rep = shseq_rep = 8
        self.shseq = shseq = pn_symbols[0:shseq_len]
        self.samp_rate = samp_rate = 1000000
        self.pilot_symbols = pilot_symbols = ((1, 1, 1, -1,),)
        self.pilot_carriers = pilot_carriers = ((-21, -7, 7, 21,),)
        self.payload_mod = payload_mod = digital.constellation_qpsk()
        self.packet_len = packet_len = 3*len(range(-26, -21)+ range(-20,-7) + range(8, 21) + range(22, 27),)
        self.ncofdm_amp = ncofdm_amp = 0
        self.lgseq = lgseq = pn_symbols[shseq_len:shseq_len+lgseq_len]
        self.header_formatter = header_formatter = digital.packet_header_ofdm(occupied_carriers, 1, length_tag_name)
        self.final_gain = final_gain = 0
        self.dataseq = dataseq = pn_symbols[shseq_len+lgseq_len:shseq_len+lgseq_len+dataseq_len]
        self.data_len = data_len = dataseq_len*20
        self.cp_len = cp_len = fft_len/4
        self.cen_freq = cen_freq = 1500000000

        ##################################################
        # Blocks
        ##################################################
        self._ncofdm_amp_layout = Qt.QVBoxLayout()
        self._ncofdm_amp_tool_bar = Qt.QToolBar(self)
        self._ncofdm_amp_layout.addWidget(self._ncofdm_amp_tool_bar)
        self._ncofdm_amp_tool_bar.addWidget(Qt.QLabel("ncofdm_amp"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._ncofdm_amp_counter = qwt_counter_pyslot()
        self._ncofdm_amp_counter.setRange(0, 2, 0.02)
        self._ncofdm_amp_counter.setNumButtons(2)
        self._ncofdm_amp_counter.setValue(self.ncofdm_amp)
        self._ncofdm_amp_tool_bar.addWidget(self._ncofdm_amp_counter)
        self._ncofdm_amp_counter.valueChanged.connect(self.set_ncofdm_amp)
        self._ncofdm_amp_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._ncofdm_amp_slider.setRange(0, 2, 0.02)
        self._ncofdm_amp_slider.setValue(self.ncofdm_amp)
        self._ncofdm_amp_slider.setMinimumWidth(200)
        self._ncofdm_amp_slider.valueChanged.connect(self.set_ncofdm_amp)
        self._ncofdm_amp_layout.addWidget(self._ncofdm_amp_slider)
        self.top_layout.addLayout(self._ncofdm_amp_layout)
        self._final_gain_layout = Qt.QVBoxLayout()
        self._final_gain_tool_bar = Qt.QToolBar(self)
        self._final_gain_layout.addWidget(self._final_gain_tool_bar)
        self._final_gain_tool_bar.addWidget(Qt.QLabel("final_gain"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._final_gain_counter = qwt_counter_pyslot()
        self._final_gain_counter.setRange(0, 1, 0.01)
        self._final_gain_counter.setNumButtons(2)
        self._final_gain_counter.setValue(self.final_gain)
        self._final_gain_tool_bar.addWidget(self._final_gain_counter)
        self._final_gain_counter.valueChanged.connect(self.set_final_gain)
        self._final_gain_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._final_gain_slider.setRange(0, 1, 0.01)
        self._final_gain_slider.setValue(self.final_gain)
        self._final_gain_slider.setMinimumWidth(200)
        self._final_gain_slider.valueChanged.connect(self.set_final_gain)
        self._final_gain_layout.addWidget(self._final_gain_slider)
        self.top_layout.addLayout(self._final_gain_layout)
        self.uhd_usrp_sink = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink.set_samp_rate(samp_rate)
        self.uhd_usrp_sink.set_center_freq(cen_freq, 0)
        self.uhd_usrp_sink.set_gain(0, 0)
        self.ncofdm_ncofdm_carrier_allocator = ncofdm.ncofdm_carrier_allocator(fft_len, occupied_carriers, (), (), "packet_len")
        self.ncofdm_add_cp_underlay = ncofdm.add_cp_underlay(fft_len, cp_len, 10, data_len, shseq_len, shseq_rep, shseq, dataseq_len, dataseq, lgseq_len, lgseq, "packet_len")
        self.fft_vxx = fft.fft_vcc(fft_len, False, (()), True, 1)
        self.digital_chunks_to_symbols = digital.chunks_to_symbols_bc((payload_mod.points()), 1)
        self.blocks_vector_source = blocks.vector_source_b(range(packet_len), True, 1, tagged_streams.make_lengthtags((packet_len,), (0,), length_tag_name))
        self.blocks_repack_bits = blocks.repack_bits_bb(8, payload_mod.bits_per_symbol(), length_tag_name, False, gr.GR_LSB_FIRST)
        self.blocks_overlaygain = blocks.multiply_const_vcc(([ncofdm_amp]*fft_len))
        self.blocks_final_gain = blocks.multiply_const_vcc((final_gain, ))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_final_gain, 0), (self.uhd_usrp_sink, 0))    
        self.connect((self.blocks_overlaygain, 0), (self.ncofdm_add_cp_underlay, 0))    
        self.connect((self.blocks_repack_bits, 0), (self.digital_chunks_to_symbols, 0))    
        self.connect((self.blocks_vector_source, 0), (self.blocks_repack_bits, 0))    
        self.connect((self.digital_chunks_to_symbols, 0), (self.ncofdm_ncofdm_carrier_allocator, 0))    
        self.connect((self.fft_vxx, 0), (self.blocks_overlaygain, 0))    
        self.connect((self.ncofdm_add_cp_underlay, 0), (self.blocks_final_gain, 0))    
        self.connect((self.ncofdm_ncofdm_carrier_allocator, 0), (self.fft_vxx, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ncofdm_tx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_shseq_len(self):
        return self.shseq_len

    def set_shseq_len(self, shseq_len):
        self.shseq_len = shseq_len
        self.set_dataseq(self.pn_symbols[self.shseq_len+self.lgseq_len:self.shseq_len+self.lgseq_len+self.dataseq_len])
        self.set_shseq(self.pn_symbols[0:self.shseq_len])
        self.set_lgseq(self.pn_symbols[self.shseq_len:self.shseq_len+self.lgseq_len])

    def get_pn_symbols(self):
        return self.pn_symbols

    def set_pn_symbols(self, pn_symbols):
        self.pn_symbols = pn_symbols
        self.set_dataseq(self.pn_symbols[self.shseq_len+self.lgseq_len:self.shseq_len+self.lgseq_len+self.dataseq_len])
        self.set_shseq(self.pn_symbols[0:self.shseq_len])
        self.set_lgseq(self.pn_symbols[self.shseq_len:self.shseq_len+self.lgseq_len])

    def get_occupied_carriers(self):
        return self.occupied_carriers

    def set_occupied_carriers(self, occupied_carriers):
        self.occupied_carriers = occupied_carriers
        self.set_header_formatter(digital.packet_header_ofdm(self.occupied_carriers, 1, self.length_tag_name))

    def get_lgseq_len(self):
        return self.lgseq_len

    def set_lgseq_len(self, lgseq_len):
        self.lgseq_len = lgseq_len
        self.set_dataseq(self.pn_symbols[self.shseq_len+self.lgseq_len:self.shseq_len+self.lgseq_len+self.dataseq_len])
        self.set_lgseq(self.pn_symbols[self.shseq_len:self.shseq_len+self.lgseq_len])

    def get_length_tag_name(self):
        return self.length_tag_name

    def set_length_tag_name(self, length_tag_name):
        self.length_tag_name = length_tag_name
        self.set_header_formatter(digital.packet_header_ofdm(self.occupied_carriers, 1, self.length_tag_name))

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len
        self.set_cp_len(self.fft_len/4)
        self.blocks_overlaygain.set_k(([self.ncofdm_amp]*self.fft_len))

    def get_dataseq_len(self):
        return self.dataseq_len

    def set_dataseq_len(self, dataseq_len):
        self.dataseq_len = dataseq_len
        self.set_data_len(self.dataseq_len*20)
        self.set_dataseq(self.pn_symbols[self.shseq_len+self.lgseq_len:self.shseq_len+self.lgseq_len+self.dataseq_len])

    def get_sync_word2(self):
        return self.sync_word2

    def set_sync_word2(self, sync_word2):
        self.sync_word2 = sync_word2

    def get_sync_word1(self):
        return self.sync_word1

    def set_sync_word1(self, sync_word1):
        self.sync_word1 = sync_word1

    def get_sync_len(self):
        return self.sync_len

    def set_sync_len(self, sync_len):
        self.sync_len = sync_len

    def get_shseq_rep(self):
        return self.shseq_rep

    def set_shseq_rep(self, shseq_rep):
        self.shseq_rep = shseq_rep

    def get_shseq(self):
        return self.shseq

    def set_shseq(self, shseq):
        self.shseq = shseq

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink.set_samp_rate(self.samp_rate)

    def get_pilot_symbols(self):
        return self.pilot_symbols

    def set_pilot_symbols(self, pilot_symbols):
        self.pilot_symbols = pilot_symbols

    def get_pilot_carriers(self):
        return self.pilot_carriers

    def set_pilot_carriers(self, pilot_carriers):
        self.pilot_carriers = pilot_carriers

    def get_payload_mod(self):
        return self.payload_mod

    def set_payload_mod(self, payload_mod):
        self.payload_mod = payload_mod

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len
        self.blocks_vector_source.set_data(range(self.packet_len))

    def get_ncofdm_amp(self):
        return self.ncofdm_amp

    def set_ncofdm_amp(self, ncofdm_amp):
        self.ncofdm_amp = ncofdm_amp
        self.blocks_overlaygain.set_k(([self.ncofdm_amp]*self.fft_len))
        Qt.QMetaObject.invokeMethod(self._ncofdm_amp_counter, "setValue", Qt.Q_ARG("double", self.ncofdm_amp))
        Qt.QMetaObject.invokeMethod(self._ncofdm_amp_slider, "setValue", Qt.Q_ARG("double", self.ncofdm_amp))

    def get_lgseq(self):
        return self.lgseq

    def set_lgseq(self, lgseq):
        self.lgseq = lgseq

    def get_header_formatter(self):
        return self.header_formatter

    def set_header_formatter(self, header_formatter):
        self.header_formatter = header_formatter

    def get_final_gain(self):
        return self.final_gain

    def set_final_gain(self, final_gain):
        self.final_gain = final_gain
        self.blocks_final_gain.set_k((self.final_gain, ))
        Qt.QMetaObject.invokeMethod(self._final_gain_counter, "setValue", Qt.Q_ARG("double", self.final_gain))
        Qt.QMetaObject.invokeMethod(self._final_gain_slider, "setValue", Qt.Q_ARG("double", self.final_gain))

    def get_dataseq(self):
        return self.dataseq

    def set_dataseq(self, dataseq):
        self.dataseq = dataseq

    def get_data_len(self):
        return self.data_len

    def set_data_len(self, data_len):
        self.data_len = data_len

    def get_cp_len(self):
        return self.cp_len

    def set_cp_len(self, cp_len):
        self.cp_len = cp_len

    def get_cen_freq(self):
        return self.cen_freq

    def set_cen_freq(self, cen_freq):
        self.cen_freq = cen_freq
        self.uhd_usrp_sink.set_center_freq(self.cen_freq, 0)

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = ncofdm_tx()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
