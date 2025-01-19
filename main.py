""" @package main

@brief Program's entry point
"""

from src.Utils import *
from src.Plotter import *
from src.Simulator import *
from src.Configurations import *
from src.ArgsHandler import *


# importing src/Logger.py initializes logging
import src.Logger

def main():
  """Run chosen simulation"""
  chosen_mode, plot_params = ThreeBodyArgParser().handle_args()
  params = chosen_mode()
  params = params | plot_params
  
  sim = ThreeBodySimulator(params)
  solution = sim.solve_system_of_equations()

  plotter = ThreeBodyPlotter(solution, params)
  plotter.plot_detailed()
  plotter.plot_phase()
  plotter.plot_phase_detailed_x()
  plotter.plot_positions()
  plotter.make_animation()

  lyapunov_sim = LyapunovAnalyzer(params)
  xs, exponents = lyapunov_sim.analyze_x0()

  lyapunov_plotter = LyapunovPlotter(xs, exponents, params)
  lyapunov_plotter.plot_lyapunov()

if __name__ == "__main__":
  main()