import numpy as np

# Constants
propconst = 8.99e9

class PointCharge():
    def __init__(self, Q, x, y):
        self.Q = Q
        self.x = x
        self.y = y

    def E_Field(self, x, y):
        effectivex = (x - self.x)
        effectivey = (y - self.y)
        mag = propconst * (self.Q / (np.sqrt(effectivex**2 + effectivey**2))**2)
        Ex = mag * (np.cos(np.arctan2(effectivey, effectivex)))
        Ey = mag * (np.sin(np.arctan2(effectivey, effectivex)))
        return Ex, Ey