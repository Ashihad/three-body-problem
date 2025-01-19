""" @package Configurations 

@brief Available system configurations

@details This module defines predefined configurations of various three body problems which can be selected from command line.
Each function defined here returns a dictionary containing all data needed for differential equation solver
to solve a given problem. Each dictionary **must** contain exactly 3 `ObjectParams2D` objects under `1`, `2` and `3`
dictionary keys, `days` parameter, and `G` parameter. Other parameters are optional, but may disable some parts
of the program (e.g. not specifying `frames` results in lack of animation generation).

Parameters overview:
- `1`/`2`/`3` - `ObjectParams2D`s containing initial conditions and masses of each body
- `G` - value of gravitational constant, some configurations run with `G == 1`, some with real life value
- `days` - upper bound of simulation time, it might be fractional (e.g. value 1/24 specifies one hour)
- `frames` - total animation frames, this parameter is directly passed to `matplotlib.animation.FuncAnimation` handler, ommitting it disables animation generation
- `title` - if set, plots will have this string displayed above them
- `phase_detailed_x` - creating such dictionary implies zoomed phase plot generation for x/vx parameters of specified body
  - `body_no` chooses a body for zoomed plot, numbers `1`, `2` and `3` are only valid imputs
  - `xrange` is a tuple of `(xrange_min, xragne_max)` for zoom plot
  - `yrange` is a tuple of `(yrange_min, yragne_max)` for zoom plot
- `lyapunov` - creating such dictionary implies generating a Lyapunov exponent plot for a given body, parameter, range of change and simulation time
  - `body_no` chooses a body for zoomed plot, numbers `1`, `2` and `3` are only valid imputs
  - `range` defines an iterable containing a range of change for a given parameter TODO this is hardcoded 
  - `param` sets a label for x axis, this argument is passed directly to `matplotlib.pyplot`
  - `days` specifies maximum simulation time for each Lyapunov exponent, it is usually shorter than normal simulation time

Usage example:
@code
  # assuming user has chosen `sun_earth_mars` configuration
  sun_earth_mars, plotting_params = ThreeBodyArgParser()

  params = sun_earth_mars()
  params = params | plot_params
  simulator = ThreeBodySimulator(params)
@endcode
"""

from .Utils import *

def sun_earth_mars():
  """Sun-Earth-Mars system
  @returns Dictionary with simulation parameters
  """
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(0, 0, 0, 0, 1.989e30)            # sun
  params['2'] = ObjectParams2D(0, 1.5e11, 29.78e3, 0, 5.97e24)  # earth
  params['3'] = ObjectParams2D(0, 2.28e11, 24.07e3, 0, 6.42e23) # mars
  params['days'] = 365
  params['frames'] = 500
  params['title'] = "Sun-Earth-Mars system"
  return params

def newton_problem():
  """Sun-Earth-Moon system
  @returns Dictionary with simulation parameters
  """
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(0, 0, 0, 0, 1.989e30)                            # sun
  params['2'] = ObjectParams2D(0, 1.5e11, 29.78e3, 0, 5.97e24)                  # earth
  params['3'] = ObjectParams2D(0, 1.5e11+384_400_000, 29.78e3+1022, 0, 7.35e22) # moon
  params['days'] = 365
  params['frames'] = 500
  params['title'] = "Newton problem (Sun-Earth-Moon system)"
  return params

def triangle():
  """Equilateral triangle
  @returns Dictionary with simulation parameters
  """
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(-np.sqrt(3)/2*1.5e11, -1/2*1.5e11, 0, 0, 1.989e32)
  params['2'] = ObjectParams2D( np.sqrt(3)/2*1.5e11, -1/2*1.5e11, 0, 0, 1.989e32)
  params['3'] = ObjectParams2D(0, 1*1.5e11, 0, 0, 1.989e32)
  params['days'] = 365
  params['frames'] = 500
  params['title'] = "Equilateral triangle configuration"
  return params

def burrau():
  """Burrau problem (3-4-5 triangle)
  @see https://en.wikipedia.org/wiki/Three-body_problem#Special-case_solutions
  @returns Dictionary with simulation parameters
  """
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(0, 0, 0, 0, 5)
  params['2'] = ObjectParams2D(-3, 0, 0, 0, 4)
  params['3'] = ObjectParams2D(0, 4, 0, 0, 3)
  params['days'] = 80
  params['frames'] = 500
  params['title'] = "Burrau problem"

  params['phase_detailed_x'] = {}
  params['phase_detailed_x']['body_no'] = 1
  params['phase_detailed_x']['xrange'] = (-1.5, -0.6)
  params['phase_detailed_x']['yrange'] = (-0.0001, 0.0001)

  params['lyapunov'] = {}
  params['lyapunov']['body_no'] = 2
  params['lyapunov']['param'] = '$x_0$'
  params['lyapunov']['range'] = np.linspace(params['2'].x_0, params['2'].x_0 + 2.999, 20)
  params['lyapunov']['days'] = 20

  return params

def burrau_shifted():
  """Burrau problem (3-4-5 triangle), shifted by 1e-6 in various directions
  @see https://en.wikipedia.org/wiki/Three-body_problem#Special-case_solutions
  @returns Dictionary with simulation parameters
  """
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(0.000001, -0.000001, 0, 0, 5)
  params['2'] = ObjectParams2D(-3.000001, 0, 0, 0, 4)
  params['3'] = ObjectParams2D(0, 4.000001, 0, 0, 3)
  params['days'] = 80
  params['frames'] = 500
  params['title'] = "Burrau problem, shifted by 1e-6"

  params['phase_detailed_x'] = {}
  params['phase_detailed_x']['body_no'] = 1
  params['phase_detailed_x']['xrange'] = (-1.5, -0.6)
  params['phase_detailed_x']['yrange'] = (-0.0001, 0.0001)

  params['lyapunov'] = {}
  params['lyapunov']['body_no'] = 2
  params['lyapunov']['param'] = '$x_0$'
  params['lyapunov']['range'] = np.linspace(params['2'].x_0, params['2'].x_0 + 2.999, 20)
  params['lyapunov']['days'] = 20

  return params

def burrau_less_shifted():
  """Burrau problem (3-4-5 triangle), shifted by 1e-12 in various directions
  @see https://en.wikipedia.org/wiki/Three-body_problem#Special-case_solutions
  @returns Dictionary with simulation parameters
  """
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(0.000000000001, -0.000000000001, 0, 0, 5)
  params['2'] = ObjectParams2D(-3.000000000001, 0, 0, 0, 4)
  params['3'] = ObjectParams2D(0, 4.000000000001, 0, 0, 3)
  params['days'] = 80
  params['frames'] = 500
  params['title'] = "Burrau problem, shifted by 1e-12"

  params['phase_detailed_x'] = {}
  params['phase_detailed_x']['body_no'] = 1
  params['phase_detailed_x']['xrange'] = (-1.5, -0.6)
  params['phase_detailed_x']['yrange'] = (-0.0001, 0.0001)

  params['lyapunov'] = {}
  params['lyapunov']['body_no'] = 2
  params['lyapunov']['param'] = '$x_0$'
  params['lyapunov']['range'] = np.linspace(params['2'].x_0, params['2'].x_0 + 2.999, 20)
  params['lyapunov']['days'] = 20

  return params

# https://arxiv.org/pdf/1705.00527

def xiaoming_li_et_all_1():
  """Example periodic configuration, from Xiaoming Li et all
  @see https://arxiv.org/pdf/1705.00527
  @returns Dictionary with simulation parameters
  """
  params = {}
  params['G'] = 1
  v1 = 0.4159559963
  v2 = 0.2988672319
  params['1'] = ObjectParams2D(-1, 0, v1, v2, 1)
  params['2'] = ObjectParams2D(1, 0, v1, v2, 1)
  params['3'] = ObjectParams2D(0, 0, -2*v1, -2*v2, 1)
  params['days'] = 1/24/60*2  # 2 minutes
  params['frames'] = 500
  params['title'] = "Xiaoming Li et al"
  return params

def xiaoming_li_et_all_2():
  """Example periodic configuration, from Xiaoming Li et all
  @see https://arxiv.org/pdf/1705.00527
  @returns Dictionary with simulation parameters
  """
  params = {}
  params['G'] = 1
  v1 = 0.3231926176
  v2 = 0.3279135713
  params['1'] = ObjectParams2D(-1, 0, v1, v2, 1)
  params['2'] = ObjectParams2D(1, 0, v1, v2, 1)
  params['3'] = ObjectParams2D(0, 0, -2*v1, -2*v2, 1)
  params['days'] = 1/24/60*2  # 2 minutes
  params['frames'] = 1000
  params['title'] = "Xiaoming Li et al"
  return params

def xiaoming_li_et_all_3():
  """Example periodic configuration, from Xiaoming Li et all
  @see https://arxiv.org/pdf/1705.00527
  @returns Dictionary with simulation parameters
  """
  params = {}
  params['G'] = 1
  v1 = 0.3369172422
  v2 = 0.2901238678
  params['1'] = ObjectParams2D(-1, 0, v1, v2, 1)
  params['2'] = ObjectParams2D(1, 0, v1, v2, 1)
  params['3'] = ObjectParams2D(0, 0, -2*v1, -2*v2, 1)
  params['days'] = 1/24/60*2  # 2 minutes
  params['frames'] = 1000
  params['title'] = "Xiaoming Li et al"
  return params

def l1():
  """Lagrange L1 point for Sun-Earth system
  @returns Dictionary with simulation parameters
  """
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(0, 0, 0, 0, 1.989e30)                            # sun
  params['2'] = ObjectParams2D(0, 1.5e11, 29.78e3, 0, 5.97e24)                  # earth
  params['3'] = ObjectParams2D(
    0, 
    1.5e11 - (1.5e11*((5.97e24/(5.97e24+1.989e30))/3)**(1/3)), 
    29.78e3, 
    0, 
    1e3
  )                    # satellite
  params['days'] = 365*2
  params['frames'] = 500
  params['title'] = "L1 Lagrange point (Sun-Earth-satellite system)"
  return params

def butterfly():
  """\"Butterfly\" configuration, from Suvakov et all
  @see https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.110.114301
  @returns Dictionary with simulation parameters
  """
  params = {}
  params['G'] = 1
  vx = 0.30689
  vy = 0.12551
  params['1'] = ObjectParams2D(-1, 0, vx, vy, 1)
  params['2'] = ObjectParams2D(1, 0, vx, vy, 1)
  params['3'] = ObjectParams2D(0, 0, -2*vx, -2*vy, 1)
  params['days'] = 1/24/60/60*12 # 12 seconds
  params['frames'] = 500
  params['title'] = "\"Butterfly\" configuration"
  return params

def bumblebee():
  """\"Bumblebee\" configuration, from Suvakov et all
  @see https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.110.114301
  @returns Dictionary with simulation parameters
  """
  params = {}
  params['G'] = 1
  vx = 0.18428
  vy = 0.58719
  params['1'] = ObjectParams2D(-1, 0, vx, vy, 1)
  params['2'] = ObjectParams2D(1, 0, vx, vy, 1)
  params['3'] = ObjectParams2D(0, 0, -2*vx, -2*vy, 1)
  params['days'] = 1/24/60/60*70 # 70 seconds
  params['frames'] = 500
  params['title'] = "\"Bumblebee\" configuration"
  return params

def goggles():
  """\"Goggles\" configuration, from Suvakov et all
  @see https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.110.114301
  @returns Dictionary with simulation parameters
  """
  params = {}
  params['G'] = 1
  vx = 0.08330
  vy = 0.12789
  params['1'] = ObjectParams2D(-1, 0, vx, vy, 1)
  params['2'] = ObjectParams2D(1, 0, vx, vy, 1)
  params['3'] = ObjectParams2D(0, 0, -2*vx, -2*vy, 1)
  params['days'] = 1/24/60/60*20 # 20 seconds
  params['frames'] = 500
  params['title'] = "\"Goggles\" configuration"
  return params

def yinyang():
  """\"Yin-Yang\" configuration, from Suvakov et all
  @see https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.110.114301
  @returns Dictionary with simulation parameters
  """
  params = {}
  params['G'] = 1
  vx = 0.51394
  vy = 0.30474
  params['1'] = ObjectParams2D(-1, 0, vx, vy, 1)
  params['2'] = ObjectParams2D(1, 0, vx, vy, 1)
  params['3'] = ObjectParams2D(0, 0, -2*vx, -2*vy, 1)
  params['days'] = 1/24/60/60*35 # 35 seconds
  params['frames'] = 500
  params['title'] = "\"Yin Yang\" configuration"
  return params
