import numpy as np
import matplotlib.pyplot as plt
from rk4_solver import rk4_step

def oscillator(y, t):
    x, v = y
    return np.array([v, -x])

dt = 0.01
steps = 2000

y = np.array([1.0, 0.0])
xs = []

for _ in range(steps):
    xs.append(y[0])
    y = rk4_step(oscillator, y, 0, dt)

plt.plot(xs)
plt.title("RK4 Test: Simple Harmonic Oscillator")
plt.xlabel("Time step")
plt.ylabel("Position")
plt.show()
