#! /usr/bin/python
# -*- coding: utf-8 -*-

# import logging
# logger = logging.getLogger(__name__)
from loguru import logger
import pytest
# import os.path
import anwa.algorithm
from pathlib import Path
import shutil

# path_to_script = os.path.dirname(os.path.abspath(__file__))
import io3d
import glob



# @pytest.mark.interactive
@pytest.mark.slow
def test_run_one_dir():
    aw = anwa.algorithm.AnimalWatch()
    aw.set_input_dir("~/data/lynx_lynx/fotopasti_20170825/videa/bez rysa/lok3/2017_01_17/")
    # aw.set_input_dir("~/data/lynx_lynx/fotopasti_20170825/videa/s rysem/**/*")
    aw.run()


def test_on_arina_with_two_different_report_levels():
    aw = anwa.algorithm.AnimalWatch()
    opath = "./test_output"
    expected_pth = Path(opath)
    logger.debug(f"expected_pth={expected_pth}")
    if expected_pth.exists():
        shutil.rmtree(expected_pth)
    # pth = "~/data/animals/orig/"
    pth = io3d.datasets.join_path("animals", "orig", get_root=True)
    # pthout = io3d.datasets.join_path("animals", "orig", get_root=True)
    aw.set_input_dir(pth)
    aw.set_report_level(90)
    aw.set_output_dir(opath)
    # aw.set_input_dir("~/data/lynx_lynx/fotopasti_20170825/videa/s rysem/**/*")
    aw.run()

    assert (expected_pth / "arina_cut.mp4").exists()
    nfiles90 = len(glob.glob(str(expected_pth / "*")))
    aw.set_report_level(10)
    aw.set_output_dir(opath)
    aw.run()
    nfiles10 = len(glob.glob(str(expected_pth / "*")))
    assert nfiles90 < nfiles10

