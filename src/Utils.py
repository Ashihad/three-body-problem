"""This module defines a dataclass which holds initial conditions of a body in three body problem.

`ObjectParams2D` objects are expected to be held inside a dictionary under keys `1`, `2` and `3`.
Each aprameter is mandatory, they can be provided in every standard way supported by `dataclasses` module.

Members overview:
- `x_0` - specifies body's initial position in x axis
- `y_0` - specifies body's initial position in y axis
- `vx_0` - specifies body's initial velocity in x axis
- `vy_0` - specifies body's initial velocity in y axis
- `m` - specifies body's mass

Usage example:
@code
  earth_x0 = 0
  earth_y0 = 1.5e11
  earth_vx0 = 29.78e3
  earth_vy0 = 0
  earth_mass = 5.97e24
  earth_like_object = ObjectParams2D(
    earth_x0,
    earth_y0,
    earth_vx0,
    earth_vy0,
    earth_mass
  )
@endcode
"""

from dataclasses import dataclass

import numpy as np

@dataclass
class ObjectParams2D:
  x_0: np.float64
  y_0: np.float64
  vx_0: np.float64
  vy_0: np.float64
  m: np.float64
