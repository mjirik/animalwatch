#! /usr/bin/python
# -*- coding: utf-8 -*-

# import logging
# logger = logging.getLogger(__name__)
from loguru import logger
import pytest
# import anwa.algorithm
import click.testing
import io3d
import shutil

# path_to_script = os.path.dirname(os.path.abspath(__file__))

# @pytest.mark.interactive
# @pytest.mark.slow
from pathlib import Path


def test_import_app_tools():
    import anwa.app_tools
    # anwa.app_tools()
    assert anwa.app_tools.create_icon is not None


# def test_import_qtexceptionhook():
#     import anwa.qtexceptionhook
#     assert anwa.qtexceptionhook.qt_exception_hook is not None


def test_main():
    import anwa.main_click

    pth = io3d.datasets.join_path("animals", "orig", get_root=True)

    logger.debug(f"pth={pth}")
    expected_pth = Path(io3d.datasets.join_path("animals", "processed", "anwa", "arina_cut.mp4", get_root=True))
    logger.debug(f"expected_pth={expected_pth}")
    if expected_pth.exists():
        shutil.rmtree(expected_pth.parent)

    runner = click.testing.CliRunner()
    # runner.invoke(anwa.main_click.nogui, ["-i", str(pth)])
    runner.invoke(anwa.main_click.run, ["nogui", "-i", pth])

    assert expected_pth.exists()

    # anwa.app_tools()

    # aw = anwa.algorithm.AnimalWatch()
    # # aw.set_input_dir("~/data/anwa/")
    # aw.set_input_dir("~/data/animals/orig/")
    # # aw.set_input_dir("~/data/lynx_lynx/fotopasti_20170825/videa/s rysem/**/*")
    # aw.run()
