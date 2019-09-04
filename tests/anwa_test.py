#! /usr/bin/python
# -*- coding: utf-8 -*-

# import logging
# logger = logging.getLogger(__name__)
from loguru import logger
import pytest
import os.path
import anwa.algorithm

path_to_script = os.path.dirname(os.path.abspath(__file__))



# @pytest.mark.interactive
# @pytest.mark.slow
def test_answer():
    aw = anwa.algorithm.AnimalWatch()
    aw.set_input_dir("~/data/lynx_lynx/fotopasti_20170825/videa/bez rysa/lok3/2017_01_17/")
    # aw.set_input_dir("~/data/lynx_lynx/fotopasti_20170825/videa/s rysem/**/*")
    aw.run()


