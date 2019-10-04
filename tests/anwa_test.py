#! /usr/bin/python
# -*- coding: utf-8 -*-

# import logging
# logger = logging.getLogger(__name__)
from loguru import logger
import pytest
# import os.path
import anwa.algorithm

# path_to_script = os.path.dirname(os.path.abspath(__file__))
import io3d



# @pytest.mark.interactive
@pytest.mark.slow
def test_run_one_dir():
    aw = anwa.algorithm.AnimalWatch()
    aw.set_input_dir("~/data/lynx_lynx/fotopasti_20170825/videa/bez rysa/lok3/2017_01_17/")
    # aw.set_input_dir("~/data/lynx_lynx/fotopasti_20170825/videa/s rysem/**/*")
    aw.run()


def test_on_arina():
    aw = anwa.algorithm.AnimalWatch()
    # pth = "~/data/animals/orig/"
    pth = io3d.datasets.join_path("animals", "orig", get_root=True)
    pthout = io3d.datasets.join_path("animals", "orig", get_root=True)
    aw.set_input_dir(pth)
    aw.set_report_level(30)
    aw.set_output_dir("./test_output")
    # aw.set_input_dir("~/data/lynx_lynx/fotopasti_20170825/videa/s rysem/**/*")
    aw.run()
