import numpy as np
import matplotlib.pyplot as plt
from double_pendulum import double_pendulum
from rk4_solver import rk4_step

# Initial conditions (slightly different to see chaos)
y0 = np.array([np.pi/2, 0, np.pi/2 + 0.001, 0])
dt = 0.01
steps = 2000

trajectory1 = []
trajectory2 = []

y = y0.copy()
for _ in range(steps):
    trajectory1.append([y[0], y[2]])
    y = rk4_step(double_pendulum, y, 0, dt)

trajectory1 = np.array(trajectory1)

# Plot theta1 vs theta2 (phase space)
plt.plot(trajectory1[:,0], trajectory1[:,1])
plt.xlabel("Theta1")
plt.ylabel("Theta2")
plt.title("Double Pendulum Phase Space")
plt.show()
