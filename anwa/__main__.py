# /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Modul is used for GUI of Lisa
"""

from loguru import logger
from .main_click import run
# import sys
# import click
# from pathlib import Path
# import ast
#
# # print("start")
# # from . import image
#
# # print("start 5")
# # print("start 6")
#
# # from scaffan import algorithm
#
# from . import algorithm
#
# CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])
#
#
# # print("Running __main__.py")
# # @batch_detect.command(context_settings=CONTEXT_SETTINGS)
# # @click.argument("image_stack_dir", type=click.Path(exists=True))
# # @click.argument("working_dir", type=click.Path())
# # @click.option("--create-icon", is_flag=True,
# #               help="Create desktop icon"
# #               )
# @click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
# @click.pass_context
# def run(ctx, *args, **kwargs):
#     if ctx.invoked_subcommand is None:
#         # click.echo('I was invoked without subcommand')
#         ctx.invoke(gui, *args, **kwargs)
#         # a.main()
#     else:
#         pass
#         click.echo("I am about to invoke %s" % ctx.invoked_subcommand)
#     pass
#
#
# # @run.command(context_settings=CONTEXT_SETTINGS, help="Set persistent values")
# # @click.option("--common-spreadsheet-file",  help="Set path for common spreadsheet file.", type=click.Path())
# # def set(common_spreadsheet_file=None):
# #     mainapp = algorithm.AnimalWatch()
# #     if common_spreadsheet_file is not None:
# #         mainapp.set_common_spreadsheet_file(path=common_spreadsheet_file)
# #         logger.info(f"Common spreadsheet file path is : {common_spreadsheet_file}")
# #         print(f"Common spreadsheet file path is : {common_spreadsheet_file}")
#
# # def print_params(params):
# #     algorithm.Scaffan().parameters.
# #     params.
#
#
# @run.command(context_settings=CONTEXT_SETTINGS)
# @click.option(
#     "--params",
#     "-p",
#     multiple=True,
#     default="",
#     nargs=2,
#     help='Set parameter. First argument is path to parameter separated by ";". Second is the value.'
#     "python -m scaffan gui -p Processing;Show True",
# )
# @click.option("--print-params", "-pp", is_flag=True, help="Print parameters")
# def gui(params, print_params):
#     mainapp = algorithm.AnimalWatch()
#     if print_params:
#         import pprint
#
#         pprint.pprint(mainapp.parameters_to_dict())
#         exit()
#     for param in params:
#         mainapp.set_parameter(param[0], value=ast.literal_eval(param[1]))
#         # mainapp.parameters.param(*param[0].split(";")).setValue(ast.literal_eval(param[1]))
#     mainapp.start_gui()
#
#
# @run.command(
#     context_settings=CONTEXT_SETTINGS, help="Create an icon on Windows platform"
# )
# def install():
#     from .app_tools import create_icon
#
#     create_icon("anwa", conda_env_name="anwa_app")
#     import platform
#
#     # print(platform.system)
#     # if platform.system() == "Windows":
#     #     import pathlib
#     #     import os.path as op
#     #     # logo_fn2 = pathlib.Path(__file__).parent / pathlib.Path("scaffan_icon512.ico")
#     #
#     #     logo_fn = op.join(op.dirname(__file__), "anwa.ico")
#     #     import win32com.client
#     #     shell = win32com.client.Dispatch("WScript.Shell")
#     #
#     #     pth = Path.home()
#     #     pth = pth / "Desktop" / Path("AnWa.lnk")
#     #     shortcut = shell.CreateShortcut(str(pth))
#     #     # cmd
#     #     # ln =  "call activate scaffan; {} -m scaffan".format(sys.executable)
#     #     shortcut.TargetPath = sys.executable
#     #     shortcut.Arguments = "-m anwa"
#     #     # shortcut.TargetPath = cmd
#     #     # shortcut.Arguments = '/C "call activate scaffan & python -m scaffan" '
#     #     shortcut.IconLocation = "{},0".format(logo_fn)
#     #     shortcut.Save()
#     # pass
#
#
# @run.command(context_settings=CONTEXT_SETTINGS)
# @click.option(
#     "--input-path",
#     "-i",
#     type=click.Path(exists=True),
#     help='Path to input directory with video files.',
# )
# @click.option(
#     "--params",
#     "-p",
#     multiple=True,
#     default="",
#     nargs=2,
#     help='Set parameter. First argument is path to parameter separated by ",". Second is the value.'
#     "python -m scaffan gui -p Processing,Show True",
# )
# def nogui(input_path, params):
#     mainapp = algorithm.AnimalWatch()
#     for param in params:
#         mainapp.parameters.param(*param[0].split(",")).setValue(
#             ast.literal_eval(param[1])
#         )
#     mainapp.set_input_dir(input_path)
#     # mainapp.start_gui()
#     mainapp.run()
#
#
# # def install():

run()
