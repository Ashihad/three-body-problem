from . import Configurations

import argparse
import os
import sys
import logging

from inspect import getmembers, isfunction

class ThreeBodyArgParser:
  def __init__(self):
    self.available_modes = getmembers(Configurations, isfunction)
    self.mode_names = [fun_name for fun_name, _ in self.available_modes]
    self.logger = logging.getLogger("main")

  def print_available_modes(self):
    return f'Available configurations: \n- {'\n- '.join(self.mode_names)}'

  def validator(self, string: str):
    if not string in self.mode_names:
      raise argparse.ArgumentTypeError(f"Mode \"{string}\" not supported\n\n{self.print_available_modes()}")
    return string

  def handle_args(self):
    self.parser = argparse.ArgumentParser(
      prog='main.py',
      formatter_class=argparse.RawDescriptionHelpFormatter, 
      description='Three Body Problem simulator: Simulate, analyze and create plots and gifs for various three body problem configurations\n',
      epilog=self.print_available_modes(),
      exit_on_error=False
    )
    self.parser.add_argument("configuration", type=self.validator, help="Specified configuration of bodies' positions, velocities and masses")
    self.parser.add_argument("--detailed-file", required=False, type=str, default="detailed_plot.png", help="Name of detailed plot file")
    self.parser.add_argument("--phase-file", required=False, type=str, default="phase_plot.png", help="Name of phase plot file")
    self.parser.add_argument("--animation-file", required=False, type=str, default="three_body_animation.gif", help="Name of animation file")
    self.parser.add_argument("-q", "--quiet", action='store_true', help="If set, no interactive windows will pop up, plots will still be saved")
    try:
      args = self.parser.parse_args()
    except argparse.ArgumentError as e:
      self.logger.critical("Exception occurred during argument parsing:")
      self.logger.critical(e)
      self.parser.print_usage()
      sys.exit(2)
    plot_params = {
      "detailed_file": args.detailed_file, 
      "phase_file": args.phase_file, 
      "animation_file": args.animation_file,
      "quiet": args.quiet
    }
    return [mode[1] for mode in self.available_modes if mode[0] == args.configuration][0], plot_params
