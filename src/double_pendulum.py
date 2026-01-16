import numpy as np
import matplotlib.pyplot as plt
from rk4_solver import rk4_step

# Double Pendulum parameters
g = 9.81
L1 = 1.0
L2 = 1.0
m1 = 1.0
m2 = 1.0

def double_pendulum(y, t):
    theta1, z1, theta2, z2 = y
    delta = theta2 - theta1

    denom1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta)**2
    denom2 = (L2 / L1) * denom1

    dtheta1 = z1
    dz1 = (m2 * L1 * z1**2 * np.sin(delta) * np.cos(delta) +
           m2 * g * np.sin(theta2) * np.cos(delta) +
           m2 * L2 * z2**2 * np.sin(delta) -
           (m1 + m2) * g * np.sin(theta1)) / denom1

    dtheta2 = z2
    dz2 = (- m2 * L2 * z2**2 * np.sin(delta) * np.cos(delta) +
           (m1 + m2) * g * np.sin(theta1) * np.cos(delta) -
           (m1 + m2) * L1 * z1**2 * np.sin(delta) -
           (m1 + m2) * g * np.sin(theta2)) / denom2

    return np.array([dtheta1, dz1, dtheta2, dz2])
