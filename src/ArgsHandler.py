""" @package ArgsHandler

@brief Parsing arguments from command line

@details This module defines ThreeBodyArgParser class which handles arguments provided via command line.
ThreeBodyArgParser returns two objects, a function that can be called to generate dictionary
containing parameters specific to chosen configuration and a seperate dictionary containing
plotting-specific information (like if `--quiet` flag was passed). This dictionaries are expected
to be merged and passed along together to other classes.

Usage example:
@code
  parser = ThreeBodyArgParser()
  configuration_generator, plot_params = parser.handle_args()
  params = configuration_generator()
  params = params | plot_params
@endcode
"""

from . import Configurations

import argparse
import sys
import logging

from inspect import getmembers, isfunction

class ThreeBodyArgParser:
  """Class that parses arguments from command line"""
  def __init__(self):
    """Constructor for ThreeBodyArgParser
    @attention List of available modes is autogenerated based on contents of `src/Configurations` module
    """
    ## Map `{function_name: function}` of functions defined in `src/Configurations`
    self.available_modes = getmembers(Configurations, isfunction)
    ## List of function names defined in `src/Configurations`
    self.mode_names = [fun_name for fun_name, _ in self.available_modes if fun_name not in ('dataclass')]
    ## Global logger reference
    self.logger = logging.getLogger("main")

  def print_available_modes(self):
    """Generates a string containing all avaliable configurations"""
    mode_list = '\n - '.join(self.mode_names)
    return f"Available configurations: \n - {mode_list}"

  def validator(self, string: str):
    """Checks if string is a valid mode name
    @param string Checked string
    @returns String passed as input if validation succeeds, None otherwise
    @throws argparse.ArgumentTypeError Thrown if string does not contain a valid mode
    """
    if not string in self.mode_names:
      raise argparse.ArgumentTypeError(f"Mode \"{string}\" not supported\n\n{self.print_available_modes()}")
    return string

  def handle_args(self):
    """
    Parse arguments from command line
    @returns A tuple containing:
    - function that generates parameters for given configuration
    - dictionary containing plotting parameters
    """
    self.parser = argparse.ArgumentParser(
      prog='main.py',
      formatter_class=argparse.RawDescriptionHelpFormatter, 
      description='Three Body Problem simulator: Simulate, analyze and create plots and gifs for various three body problem configurations\n',
      epilog=self.print_available_modes(),
      exit_on_error=False
    )

    self.parser.add_argument("configuration", type=self.validator, help="Specified configuration of bodies' positions, velocities and masses, mandatory")
    self.parser.add_argument("--detailed-file", required=False, type=str, default="detailed_plot.png", help="Name of detailed plot file, optional")
    self.parser.add_argument("--trajectories-file", required=False, type=str, default="trajectories_plot.png", help="Name of trajectories plot file, optional")
    self.parser.add_argument("--phase-file", required=False, type=str, default="phase_plot.png", help="Name of phase plot file, optional")
    self.parser.add_argument("--detailed-phase-file", required=False, type=str, default="detailed_phase_plot.png", help="Name of detailed phase plot file, optional")
    self.parser.add_argument("--animation-file", required=False, type=str, default="three_body_animation.gif", help="Name of animation file, optional")
    self.parser.add_argument("--lyapunov-file", required=False, type=str, default="lyapunov.png", help="Name of Lyapunov exponent plot file, optional")
    self.parser.add_argument("-q", "--quiet", action='store_true', help="If set, no interactive windows will pop up, plots will still be saved, optional")

    try:
      args = self.parser.parse_args()
    except argparse.ArgumentError as e:
      self.logger.critical("Exception occurred during argument parsing:")
      self.logger.critical(e)
      self.parser.print_usage()
      sys.exit(2)
    
    plot_params = {
      "detailed_file": args.detailed_file,
      "trajectories_file": args.trajectories_file,
      "phase_file": args.phase_file,
      "detailed_phase_file": args.detailed_phase_file,
      "animation_file": args.animation_file,
      "lyapunov_file": args.lyapunov_file,
      "quiet": args.quiet
    }
    return [mode[1] for mode in self.available_modes if mode[0] == args.configuration][0], plot_params
