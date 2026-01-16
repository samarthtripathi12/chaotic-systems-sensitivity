import numpy as np
import matplotlib.pyplot as plt
from double_pendulum import double_pendulum
from rk4_solver import rk4_step

# Initial conditions
y1 = np.array([np.pi/2, 0, np.pi/2, 0])
y2 = np.array([np.pi/2 + 0.001, 0, np.pi/2, 0])  # tiny difference

dt = 0.01
steps = 2000

# Store positions
theta1_diff = []

for _ in range(steps):
    # Advance both systems
    y1 = rk4_step(double_pendulum, y1, 0, dt)
    y2 = rk4_step(double_pendulum, y2, 0, dt)

    # Compute Euclidean distance between angles
    diff = np.sqrt((y1[0]-y2[0])**2 + (y1[2]-y2[2])**2)
    theta1_diff.append(diff)

# Plot divergence over time
plt.plot(theta1_diff)
plt.xlabel("Time step")
plt.ylabel("Difference in angles")
plt.title("Divergence of Double Pendulum Trajectories (Chaos)")
plt.show()
