#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: NC-OFDM loopback
# Description: Example of an NC-OFDM
# Generated: Sun Dec  6 12:02:52 2015
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio.digital.utils import tagged_streams
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import math
import ncofdm
import numpy
import random
import sys

from distutils.version import StrictVersion
class ncofdm_loopback(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "NC-OFDM loopback")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("NC-OFDM loopback")
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

        self.settings = Qt.QSettings("GNU Radio", "ncofdm_loopback")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.pn_symbols = pn_symbols = (1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, 1, -1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, 1)
        self.occupied_carriers = occupied_carriers = (range(-31,32),)
        self.length_tag_name = length_tag_name = "packet_len"
        self.fft_len = fft_len = 64
        self.ShSeqLen = ShSeqLen = 40
        self.LgSeqLen = LgSeqLen = 320
        self.DataSeqLen = DataSeqLen = 64
        self.sync_len = sync_len = 20
        self.samp_rate = samp_rate = 100000
        self.pilot_symbols = pilot_symbols = ((1, 1, 1, -1,),)
        self.pilot_carriers = pilot_carriers = ((-21, -7, 7, 21,),)
        self.payload_mod = payload_mod = digital.constellation_qpsk()
        self.packet_len = packet_len = 100
        self.ncofdm_amp = ncofdm_amp = 1
        self.header_formatter = header_formatter = digital.packet_header_ofdm(occupied_carriers, 1, length_tag_name)
        self.fileprefix = fileprefix = "/root/"
        self.cp_len = cp_len = fft_len/4
        self.cen_freq = cen_freq = 1500000000
        self.ShThreshold = ShThreshold = 10
        self.ShSymbols = ShSymbols = pn_symbols[0:ShSeqLen]
        self.ShSeqRep = ShSeqRep = 8
        self.ShRepThreshold = ShRepThreshold = 3.5
        self.LgThreshold = LgThreshold = 100
        self.LgSymbols = LgSymbols = pn_symbols[ShSeqLen:ShSeqLen+LgSeqLen]
        self.DataSymbols = DataSymbols = pn_symbols[ShSeqLen+LgSeqLen:DataSeqLen+ShSeqLen+LgSeqLen]
        self.DataLen = DataLen = DataSeqLen*20

        ##################################################
        # Blocks
        ##################################################
        self.ncofdm_stream2fftvector_0 = ncofdm.stream2fftvector(fft_len, cp_len)
        self.ncofdm_ncofdm_carrier_allocator_0 = ncofdm.ncofdm_carrier_allocator(fft_len, occupied_carriers, (), (), "packet_len")
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
        self._ncofdm_amp_counter.setRange(0, 2, 0.001)
        self._ncofdm_amp_counter.setNumButtons(2)
        self._ncofdm_amp_counter.setValue(self.ncofdm_amp)
        self._ncofdm_amp_tool_bar.addWidget(self._ncofdm_amp_counter)
        self._ncofdm_amp_counter.valueChanged.connect(self.set_ncofdm_amp)
        self._ncofdm_amp_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._ncofdm_amp_slider.setRange(0, 2, 0.001)
        self._ncofdm_amp_slider.setValue(self.ncofdm_amp)
        self._ncofdm_amp_slider.setMinimumWidth(200)
        self._ncofdm_amp_slider.valueChanged.connect(self.set_ncofdm_amp)
        self._ncofdm_amp_layout.addWidget(self._ncofdm_amp_slider)
        self.top_layout.addLayout(self._ncofdm_amp_layout)
        self.ncofdm_add_cp_underlay_0 = ncofdm.add_cp_underlay(fft_len, cp_len, 20, 1280, ShSeqLen, ShSeqRep, ShSymbols, DataSeqLen, DataSymbols, LgSeqLen, LgSymbols, "packet_len")
        self.ncofdm_ShortPNdetector_0 = ncofdm.ShortPNdetector(fft_len, cp_len, ShSeqRep, ShSeqLen, 1)
        self.ncofdm_ShortPNcorr_0 = ncofdm.ShortPNcorr(fft_len, cp_len, ShSeqRep, ShSeqLen, (ShSymbols))
        self.ncofdm_LongPNcorrV2_0 = ncofdm.LongPNcorrV2(fft_len, cp_len, LgSeqLen, (LgSymbols), 60, ShSeqRep*ShSeqLen+LgSeqLen+DataLen+10)
        self.ncofdm_FreqOffCalc_0 = ncofdm.FreqOffCalc(fft_len, fft_len/4, ShSeqLen, ShSeqRep)
        self.fft_vxx_1 = fft.fft_vcc(fft_len, True, (), True, 1)
        self.fft_vxx_0 = fft.fft_vcc(fft_len, False, (()), True, 1)
        self.digital_chunks_to_symbols_xx_0_0_0 = digital.chunks_to_symbols_bc((payload_mod.points()), 1)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=0,
        	frequency_offset=0.0004,
        	epsilon=1.0,
        	taps=(1, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_vector_to_stream_0_1 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_len)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_len)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_threshold_ff_0_0 = blocks.threshold_ff(ShRepThreshold, ShRepThreshold, 0)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, packet_len, "packet_len")
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(8, payload_mod.bits_per_symbol(), length_tag_name, False, gr.GR_LSB_FIRST)
        self.blocks_null_sink_1_0_0_0_1_1_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_1_0_0_0_1_1_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_1_0_0_0_1_0_0_0 = blocks.null_sink(gr.sizeof_int*1)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc(([1/(math.sqrt(44))]*fft_len))
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(100, 0.01, 4000)
        self.blocks_float_to_int_0 = blocks.float_to_int(1, 1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_sink_1_0_0_0_3 = blocks.file_sink(gr.sizeof_gr_complex*1, fileprefix+"short.dat", False)
        self.blocks_file_sink_1_0_0_0_3.set_unbuffered(False)
        self.blocks_file_sink_1_0_0_0_2 = blocks.file_sink(gr.sizeof_gr_complex*1, fileprefix+"org.dat", False)
        self.blocks_file_sink_1_0_0_0_2.set_unbuffered(False)
        self.blocks_file_sink_1_0_0_0_1_1_1 = blocks.file_sink(gr.sizeof_float*1, fileprefix+"rxshth.dat", False)
        self.blocks_file_sink_1_0_0_0_1_1_1.set_unbuffered(False)
        self.blocks_file_sink_1_0_0_0_1_1_0 = blocks.file_sink(gr.sizeof_float*1, fileprefix+"lgth.dat", False)
        self.blocks_file_sink_1_0_0_0_1_1_0.set_unbuffered(False)
        self.blocks_file_sink_1_0_0_0_0_2_0 = blocks.file_sink(gr.sizeof_gr_complex*1, fileprefix+"txdata.dat", False)
        self.blocks_file_sink_1_0_0_0_0_2_0.set_unbuffered(False)
        self.blocks_file_sink_1_0_0_0_0_2 = blocks.file_sink(gr.sizeof_gr_complex*1, fileprefix+"rxd.dat", False)
        self.blocks_file_sink_1_0_0_0_0_2.set_unbuffered(False)
        self.blocks_file_sink_1_0_0_0_0_0 = blocks.file_sink(gr.sizeof_int*1, fileprefix+"corr.dat", False)
        self.blocks_file_sink_1_0_0_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_1_0_0_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, fileprefix+"dec.dat", False)
        self.blocks_file_sink_1_0_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_1_0_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, fileprefix+"long.dat", False)
        self.blocks_file_sink_1_0_0_0.set_unbuffered(False)
        self.blocks_delay_0_0_0_0_0_0_0 = blocks.delay(gr.sizeof_float*1, 2)
        self.blocks_delay_0_0_0_0_0_0 = blocks.delay(gr.sizeof_float*1, 2)
        self.blocks_delay_0_0_0_0_0 = blocks.delay(gr.sizeof_int*1, 1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_mag_0_0_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 200, 10000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.ncofdm_ShortPNdetector_0, 0))    
        self.connect((self.blocks_complex_to_mag_0_0_0, 0), (self.blocks_moving_average_xx_0, 0))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_file_sink_1_0_0_0_1_1_0, 0))    
        self.connect((self.blocks_delay_0_0_0_0_0, 0), (self.ncofdm_FreqOffCalc_0, 1))    
        self.connect((self.blocks_delay_0_0_0_0_0_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.blocks_delay_0_0_0_0_0_0_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.ncofdm_LongPNcorrV2_0, 1))    
        self.connect((self.blocks_float_to_int_0, 0), (self.blocks_delay_0_0_0_0_0, 0))    
        self.connect((self.blocks_moving_average_xx_0, 0), (self.ncofdm_LongPNcorrV2_0, 2))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.ncofdm_add_cp_underlay_0, 0))    
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.digital_chunks_to_symbols_xx_0_0_0, 0))    
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_repack_bits_bb_0_0, 0))    
        self.connect((self.blocks_threshold_ff_0_0, 0), (self.blocks_delay_0_0_0_0_0_0, 0))    
        self.connect((self.blocks_threshold_ff_0_0, 0), (self.blocks_float_to_int_0, 0))    
        self.connect((self.blocks_throttle_0_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_file_sink_1_0_0_0_0, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_null_sink_1, 0))    
        self.connect((self.blocks_vector_to_stream_0_1, 0), (self.blocks_file_sink_1_0_0_0_0_2, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.blocks_complex_to_mag_0_0_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.blocks_file_sink_1_0_0_0_2, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.ncofdm_LongPNcorrV2_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.ncofdm_ShortPNcorr_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.ncofdm_stream2fftvector_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0_0_0, 0), (self.ncofdm_ncofdm_carrier_allocator_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.fft_vxx_1, 0), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.ncofdm_FreqOffCalc_0, 0), (self.blocks_delay_0_0_0_0_0_0_0, 0))    
        self.connect((self.ncofdm_LongPNcorrV2_0, 0), (self.blocks_complex_to_real_0, 0))    
        self.connect((self.ncofdm_LongPNcorrV2_0, 1), (self.blocks_file_sink_1_0_0_0, 0))    
        self.connect((self.ncofdm_LongPNcorrV2_0, 2), (self.blocks_file_sink_1_0_0_0_0_0, 0))    
        self.connect((self.ncofdm_LongPNcorrV2_0, 2), (self.blocks_null_sink_1_0_0_0_1_0_0_0, 0))    
        self.connect((self.ncofdm_LongPNcorrV2_0, 1), (self.blocks_null_sink_1_0_0_0_1_1_0, 0))    
        self.connect((self.ncofdm_LongPNcorrV2_0, 0), (self.blocks_null_sink_1_0_0_0_1_1_0_0, 0))    
        self.connect((self.ncofdm_LongPNcorrV2_0, 2), (self.ncofdm_stream2fftvector_0, 1))    
        self.connect((self.ncofdm_ShortPNcorr_0, 1), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.ncofdm_ShortPNcorr_0, 1), (self.blocks_file_sink_1_0_0_0_3, 0))    
        self.connect((self.ncofdm_ShortPNcorr_0, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.ncofdm_ShortPNcorr_0, 1), (self.ncofdm_FreqOffCalc_0, 0))    
        self.connect((self.ncofdm_ShortPNdetector_0, 1), (self.blocks_file_sink_1_0_0_0_1_1_1, 0))    
        self.connect((self.ncofdm_ShortPNdetector_0, 0), (self.blocks_threshold_ff_0_0, 0))    
        self.connect((self.ncofdm_add_cp_underlay_0, 0), (self.blocks_file_sink_1_0_0_0_0_2_0, 0))    
        self.connect((self.ncofdm_add_cp_underlay_0, 0), (self.blocks_throttle_0_0, 0))    
        self.connect((self.ncofdm_ncofdm_carrier_allocator_0, 0), (self.blocks_vector_to_stream_0_1, 0))    
        self.connect((self.ncofdm_ncofdm_carrier_allocator_0, 0), (self.fft_vxx_0, 0))    
        self.connect((self.ncofdm_stream2fftvector_0, 0), (self.fft_vxx_1, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ncofdm_loopback")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_pn_symbols(self):
        return self.pn_symbols

    def set_pn_symbols(self, pn_symbols):
        self.pn_symbols = pn_symbols
        self.set_DataSymbols(self.pn_symbols[self.ShSeqLen+self.LgSeqLen:self.DataSeqLen+self.ShSeqLen+self.LgSeqLen])
        self.set_LgSymbols(self.pn_symbols[self.ShSeqLen:self.ShSeqLen+self.LgSeqLen])
        self.set_ShSymbols(self.pn_symbols[0:self.ShSeqLen])

    def get_occupied_carriers(self):
        return self.occupied_carriers

    def set_occupied_carriers(self, occupied_carriers):
        self.occupied_carriers = occupied_carriers
        self.set_header_formatter(digital.packet_header_ofdm(self.occupied_carriers, 1, self.length_tag_name))

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
        self.blocks_multiply_const_vxx_0_0.set_k(([1/(math.sqrt(44))]*self.fft_len))

    def get_ShSeqLen(self):
        return self.ShSeqLen

    def set_ShSeqLen(self, ShSeqLen):
        self.ShSeqLen = ShSeqLen
        self.set_DataSymbols(self.pn_symbols[self.ShSeqLen+self.LgSeqLen:self.DataSeqLen+self.ShSeqLen+self.LgSeqLen])
        self.set_LgSymbols(self.pn_symbols[self.ShSeqLen:self.ShSeqLen+self.LgSeqLen])
        self.set_ShSymbols(self.pn_symbols[0:self.ShSeqLen])

    def get_LgSeqLen(self):
        return self.LgSeqLen

    def set_LgSeqLen(self, LgSeqLen):
        self.LgSeqLen = LgSeqLen
        self.set_DataSymbols(self.pn_symbols[self.ShSeqLen+self.LgSeqLen:self.DataSeqLen+self.ShSeqLen+self.LgSeqLen])
        self.set_LgSymbols(self.pn_symbols[self.ShSeqLen:self.ShSeqLen+self.LgSeqLen])

    def get_DataSeqLen(self):
        return self.DataSeqLen

    def set_DataSeqLen(self, DataSeqLen):
        self.DataSeqLen = DataSeqLen
        self.set_DataLen(self.DataSeqLen*20)
        self.set_DataSymbols(self.pn_symbols[self.ShSeqLen+self.LgSeqLen:self.DataSeqLen+self.ShSeqLen+self.LgSeqLen])

    def get_sync_len(self):
        return self.sync_len

    def set_sync_len(self, sync_len):
        self.sync_len = sync_len

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)

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

    def get_ncofdm_amp(self):
        return self.ncofdm_amp

    def set_ncofdm_amp(self, ncofdm_amp):
        self.ncofdm_amp = ncofdm_amp
        Qt.QMetaObject.invokeMethod(self._ncofdm_amp_counter, "setValue", Qt.Q_ARG("double", self.ncofdm_amp))
        Qt.QMetaObject.invokeMethod(self._ncofdm_amp_slider, "setValue", Qt.Q_ARG("double", self.ncofdm_amp))

    def get_header_formatter(self):
        return self.header_formatter

    def set_header_formatter(self, header_formatter):
        self.header_formatter = header_formatter

    def get_fileprefix(self):
        return self.fileprefix

    def set_fileprefix(self, fileprefix):
        self.fileprefix = fileprefix
        self.blocks_file_sink_1_0_0_0_1_1_1.open(self.fileprefix+"rxshth.dat")
        self.blocks_file_sink_1_0_0_0_0_0.open(self.fileprefix+"corr.dat")
        self.blocks_file_sink_1_0_0_0_1_1_0.open(self.fileprefix+"lgth.dat")
        self.blocks_file_sink_1_0_0_0_0.open(self.fileprefix+"dec.dat")
        self.blocks_file_sink_1_0_0_0.open(self.fileprefix+"long.dat")
        self.blocks_file_sink_1_0_0_0_2.open(self.fileprefix+"org.dat")
        self.blocks_file_sink_1_0_0_0_0_2.open(self.fileprefix+"rxd.dat")
        self.blocks_file_sink_1_0_0_0_3.open(self.fileprefix+"short.dat")
        self.blocks_file_sink_1_0_0_0_0_2_0.open(self.fileprefix+"txdata.dat")

    def get_cp_len(self):
        return self.cp_len

    def set_cp_len(self, cp_len):
        self.cp_len = cp_len

    def get_cen_freq(self):
        return self.cen_freq

    def set_cen_freq(self, cen_freq):
        self.cen_freq = cen_freq

    def get_ShThreshold(self):
        return self.ShThreshold

    def set_ShThreshold(self, ShThreshold):
        self.ShThreshold = ShThreshold

    def get_ShSymbols(self):
        return self.ShSymbols

    def set_ShSymbols(self, ShSymbols):
        self.ShSymbols = ShSymbols

    def get_ShSeqRep(self):
        return self.ShSeqRep

    def set_ShSeqRep(self, ShSeqRep):
        self.ShSeqRep = ShSeqRep

    def get_ShRepThreshold(self):
        return self.ShRepThreshold

    def set_ShRepThreshold(self, ShRepThreshold):
        self.ShRepThreshold = ShRepThreshold
        self.blocks_threshold_ff_0_0.set_hi(self.ShRepThreshold)
        self.blocks_threshold_ff_0_0.set_lo(self.ShRepThreshold)

    def get_LgThreshold(self):
        return self.LgThreshold

    def set_LgThreshold(self, LgThreshold):
        self.LgThreshold = LgThreshold

    def get_LgSymbols(self):
        return self.LgSymbols

    def set_LgSymbols(self, LgSymbols):
        self.LgSymbols = LgSymbols

    def get_DataSymbols(self):
        return self.DataSymbols

    def set_DataSymbols(self, DataSymbols):
        self.DataSymbols = DataSymbols

    def get_DataLen(self):
        return self.DataLen

    def set_DataLen(self, DataLen):
        self.DataLen = DataLen

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
    tb = ncofdm_loopback()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
