from dataclasses import dataclass

import numpy as np

@dataclass
class ObjectParams2D:
  x_0: np.float64
  y_0: np.float64
  vx_0: np.float64
  vy_0: np.float64
  m: np.float64
