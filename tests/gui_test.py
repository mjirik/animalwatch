#! /usr/bin/python
# -*- coding: utf-8 -*-

from loguru import logger
import pytest
import anwa
from PyQt5 import QtWidgets
import sys


def test_gui():
    qapp = QtWidgets.QApplication(sys.argv)
    aw = anwa.algorithm.AnimalWatch()
    aw.start_gui(skip_exec=True, qapp=qapp)
