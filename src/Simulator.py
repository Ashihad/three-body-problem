from .Utils import *

from scipy.integrate import solve_ivp

import logging

class ThreeBodySimulator:

  def __init__(self, system_params):
    self.params = system_params
    self.logger = logging.getLogger("main")

  def system_of_equations(self, t, state):
    """
    Define a system of 6 coupled 2nd order differential equations.
    
    Parameters:
    t (float): Time
    Y (array): State vector 
    [x1, x2, x3, x4, x5, x6, 
      dx1/dt, dx2/dt, dx3/dt, dx4/dt, dx5/dt, dx6/dt]
    
    Returns:
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
