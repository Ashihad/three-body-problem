from src.Params import *
from src.Plotter import *
from src.Simulator import *


def main():
  # first_body_params_2D = ObjectParams2D(-np.sqrt(3)/2, 1/2, 0, 0, 1)
  # second_body_params_2D = ObjectParams2D( np.sqrt(3)/2, 1/2, 0, 0, 1)
  # third_body_params_2D = ObjectParams2D(0, 1, 0, 0, 1)
  first_body_params_2D = ObjectParams2D(0, 0, 0, 0, 1.989e30) # sun-like
  second_body_params_2D = ObjectParams2D(0, 1.5e11, 29.78e3, 0, 5.97e24) # earth-like
  third_body_params_2D = ObjectParams2D(0, 2.28e11, 24.07e3, 0, 6.42e23)  # mars-like

  params = {}
  params['1'] = first_body_params_2D
  params['2'] = second_body_params_2D
  params['3'] = third_body_params_2D

  params['g'] = 6.67430e-11
  
  sim = ThreeBodySimulator(params)
  solution = sim.solve_system_of_equations()

  plotter = ThreeBodyPlotter(solution)
  plotter.make_gif()


if __name__ == "__main__":
  main()