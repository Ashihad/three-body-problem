from src.Utils import *
from src.Plotter import *
from src.Simulator import *
from src.Configurations import *
from src.ArgsHandler import *

import src.Logger

def main():
  chosen_mode, plot_params = ThreeBodyArgParser().handle_args()
  params = chosen_mode()
  params = params | plot_params
  
  sim = ThreeBodySimulator(params)
  solution = sim.solve_system_of_equations()

  plotter = ThreeBodyPlotter(solution, params)
  plotter.plot_detailed()
  plotter.plot_phase()
  plotter.make_animation()

  # exponents = sim.lyapunov_1st_x0()
  # plotter.plot_lyapunov(exponents)

if __name__ == "__main__":
  main()