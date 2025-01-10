from src.Utils import *
from src.Plotter import *
from src.Simulator import *

def sun_earth_mars():
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(0, 0, 0, 0, 1.989e30)            # sun
  params['2'] = ObjectParams2D(0, 1.5e11, 29.78e3, 0, 5.97e24)  # earth
  params['3'] = ObjectParams2D(0, 2.28e11, 24.07e3, 0, 6.42e23) # mars
  params['days'] = 365
  return params

def newton_problem():
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(0, 0, 0, 0, 1.989e30)                            # sun
  params['2'] = ObjectParams2D(0, 1.5e11, 29.78e3, 0, 5.97e24)                  # earth
  params['3'] = ObjectParams2D(0, 1.5e11+384_400_000, 29.78e3+1022, 0, 7.35e22) # moon
  params['days'] = 31
  return params

def triangle():
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(-np.sqrt(3)/2*1.5e11, -1/2*1.5e11, 0, 0, 1.989e32)
  params['2'] = ObjectParams2D( np.sqrt(3)/2*1.5e11, -1/2*1.5e11, 0, 0, 1.989e32)
  params['3'] = ObjectParams2D(0, 1*1.5e11, 0, 0, 1.989e32)
  params['days'] = 365
  return params

def rotating_triangle():
  # does not work
  params = {}
  # params['1'] = ObjectParams2D(-np.sqrt(3)/2*1.5e11, -1/2*1.5e11, -500, 500*np.sqrt(3), 1.989e32)
  # params['2'] = ObjectParams2D( np.sqrt(3)/2*1.5e11, -1/2*1.5e11, -500*np.sqrt(3), -500, 1.989e32)
  # params['3'] = ObjectParams2D(0, 1*1.5e11, 1000, 0, 1.989e32)
  params['G'] = 6.67430e-11
  v1 = np.sqrt(6.67430e-11 * 3*1.989e32 / 1*1.5e11)/1000
  params['1'] = ObjectParams2D(-np.sqrt(3)/2*1.5e11, -1/2*1.5e11, -1/2*v1, v1*np.sqrt(3), 1.989e32)
  params['2'] = ObjectParams2D( np.sqrt(3)/2*1.5e11, -1/2*1.5e11, -v1*np.sqrt(3), -1/2*v1, 1.989e32)
  params['3'] = ObjectParams2D(0, 1*1.5e11, v1, 0, 1.989e32)
  params['days'] = 365
  return params

def burrau():
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(0, 0, 0, 0, 5)
  params['2'] = ObjectParams2D(-3, 0, 0, 0, 4)
  params['3'] = ObjectParams2D(0, 4, 0, 0, 3)
  params['days'] = 80
  return params

def burrau_tilted():
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(0.000001, -0.000001, 0, 0, 5)
  params['2'] = ObjectParams2D(-3.000001, 0, 0, 0, 4)
  params['3'] = ObjectParams2D(0, 4.000001, 0, 0, 3)
  params['days'] = 80
  return params

def xiaoming_li_et_all_1():
  # December 2017
  params = {}
  params['G'] = 1
  v1 = 0.4159559963
  v2 = 0.2988672319
  params['1'] = ObjectParams2D(-1, 0, v1, v2, 1)
  params['2'] = ObjectParams2D(1, 0, v1, v2, 1)
  params['3'] = ObjectParams2D(0, 0, -2*v1, -2*v2, 1)
  params['days'] = 31
  return params

def main():
  params = xiaoming_li_et_all_1()
  
  sim = ThreeBodySimulator(params)
  solution = sim.solve_system_of_equations()

  plotter = ThreeBodyPlotter(solution)
  plotter.make_gif(5000)


if __name__ == "__main__":
  main()