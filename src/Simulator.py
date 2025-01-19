""" @package Simulator

@brief Differential equation solvers

@details 

Example usage:
@code

@endcode

"""


from .Utils import *

from scipy.integrate import solve_ivp
from tqdm import tqdm

import logging
import sys
import copy

class ThreeBodySimulator:
  """Class that generates solution of a three body problem given simulation parameters"""
  def __init__(self, system_params):
    ## Simulator parameters
    self.params = system_params
    ## Global logger reference
    self.logger = logging.getLogger("main")

  def system_of_equations(self, t, state):
    """Defines a system of 6 coupled 2nd order differential equations.
    @param t (float): Time
    @param Y (array): State vector 
    [x1, x2, x3, x4, x5, x6, 
      dx1/dt, dx2/dt, dx3/dt, dx4/dt, dx5/dt, dx6/dt]
    @returns:
    array: Derivatives for each variable
    """
    # Unpack the state vector
    x_1, y_1, x_2, y_2, x_3, y_3, \
    dx_1, dy_1, dx_2, dy_2, dx_3, dy_3 = state

    r12 = np.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)
    r13 = np.sqrt((x_1 - x_3)**2 + (y_1 - y_3)**2)
    r23 = np.sqrt((x_2 - x_3)**2 + (y_2 - y_3)**2)
    
    # Second derivatives (from three-body problem equations)
    d2x1_dt2 = -self.params['G'] * self.params['2'].m * (x_1 - x_2)/r12**3 - \
                self.params['G'] * self.params['3'].m * (x_1 - x_3)/r13**3
    d2y1_dt2 = -self.params['G'] * self.params['2'].m * (y_1 - y_2)/r12**3 - \
                self.params['G'] * self.params['3'].m * (y_1 - y_3)/r13**3
    d2x2_dt2 = -self.params['G'] * self.params['3'].m * (x_2 - x_3)/r23**3 - \
                self.params['G'] * self.params['1'].m * (x_2 - x_1)/r12**3
    d2y2_dt2 = -self.params['G'] * self.params['3'].m * (y_2 - y_3)/r23**3 - \
                self.params['G'] * self.params['1'].m * (y_2 - y_1)/r12**3
    d2x3_dt2 = -self.params['G'] * self.params['1'].m * (x_3 - x_1)/r13**3 - \
                self.params['G'] * self.params['2'].m * (x_3 - x_2)/r23**3
    d2y3_dt2 = -self.params['G'] * self.params['1'].m * (y_3 - y_1)/r13**3 - \
                self.params['G'] * self.params['2'].m * (y_3 - y_2)/r23**3

    # Return derivatives in order: 
    # dx1/dt, dx2/dt, dx3/dt, dx4/dt, dx5/dt, dx6/dt, 
    # d2x1/dt2, d2x2/dt2, d2x3/dt2, d2x4/dt2, d2x5/dt2, d2x6/dt2
    return np.array([
        dx_1, dy_1, dx_2, dy_2, dx_3, dy_3,  # First derivatives
        d2x1_dt2, d2y1_dt2, d2x2_dt2, d2y2_dt2, d2x3_dt2, d2y3_dt2  # Second derivatives
    ])
  
  def solve_system_of_equations(self):
    """Solve system of PDEs reflecting a three body problem
    @returns OdeSolution object containing solutions for all parameters
    """
    # Initial conditions:
    # [x1, x2, x3, x4, x5, x6, dx1/dt, dx2/dt, dx3/dt, dx4/dt, dx5/dt, dx6/dt]    
    initial_conditions = [
      self.params['1'].x_0,
      self.params['1'].y_0,
      self.params['2'].x_0,
      self.params['2'].y_0,
      self.params['3'].x_0,
      self.params['3'].y_0,

      self.params['1'].vx_0,
      self.params['1'].vy_0,
      self.params['2'].vx_0,
      self.params['2'].vy_0,
      self.params['3'].vx_0,
      self.params['3'].vy_0
    ]
    
    # Time span for integration
    t_span = (0, self.params['days'] * 24 * 3600)
    
    # Solve the system of differential equations
    self.logger.info("Solving problem...")
    solution = solve_ivp(
        self.system_of_equations, 
        t_span, 
        initial_conditions,
        dense_output=True,  # Allow interpolation of solution
        rtol=1e-8,  # Relative tolerance
        atol=1e-8   # Absolute tolerance
    )
    self.logger.info("Solving done")

    return solution

class LyapunovAnalyzer(ThreeBodySimulator):
  """Class that generates an array of Lyapunov exponents for a given range of x_0 parameters for a specified body"""
  def solve_system_of_equations(self):
    """Modified solver, with looser tolerances, disabled dense output, disabled logging and using Lyapunov days range.
    It is meant to run faster and quieter, making it suitable for calling in a loop.
    @returns OdeSolution object containing solutions for all parameters
    """
    # Initial conditions:
    # [x1, x2, x3, x4, x5, x6, dx1/dt, dx2/dt, dx3/dt, dx4/dt, dx5/dt, dx6/dt]    
    initial_conditions = [
      self.params['1'].x_0,
      self.params['1'].y_0,
      self.params['2'].x_0,
      self.params['2'].y_0,
      self.params['3'].x_0,
      self.params['3'].y_0,

      self.params['1'].vx_0,
      self.params['1'].vy_0,
      self.params['2'].vx_0,
      self.params['2'].vy_0,
      self.params['3'].vx_0,
      self.params['3'].vy_0
    ]
    
    # Time span for integration
    t_span = (0, self.params['lyapunov']['days'] * 24 * 3600)
    
    # Solve the system of differential equations
    solution = solve_ivp(
        self.system_of_equations, 
        t_span, 
        initial_conditions,
        dense_output=False,  # No interpoaltion
        rtol=1e-6,  # Relative tolerance
        atol=1e-6   # Absolute tolerance
    )

    return solution

  def analyze_x0(self):
    """Calculate Lyapunov exponents from x_0s of a given body
    @returns A tuple containing:
    - used x_0 range for a given body
    - `np.array` of exponents
    """
    # check if Lyapunov exponent params are set, if not exit
    if not self.params.get('lyapunov', None):
      return
    body_no =  self.params['lyapunov']['body_no']
    
    params_bak = copy.deepcopy(self.params)
    local_params = copy.deepcopy(self.params)

    parameter_range = self.params['lyapunov']['range']

    self.logger.warning(f"Calculating Lyapunov exponents for range ({parameter_range[0]:.2f}, {parameter_range[-1]:.2f}, {len(parameter_range)}), it will take some time")
    exponents = []
    for new_x_0 in tqdm(parameter_range, total=parameter_range.size, file=sys.stdout):
      self.logger.debug(f"new_x_0={new_x_0}")

      local_params[str(body_no)].x_0 = new_x_0
      self.params = copy.deepcopy(local_params)

      solution = self.solve_system_of_equations()
      x_0_s = solution.y[2*(body_no-1)]

      # calculate lyapunov exponent from x_0s of appropriate body
      exponents.append(np.mean(np.log(np.abs(np.diff(x_0_s)))))

    self.params = params_bak
    return parameter_range, np.array(exponents)