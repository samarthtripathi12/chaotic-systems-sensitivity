import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from double_pendulum import double_pendulum
from rk4_solver import rk4_step

# Parameters
dt = 0.02
steps = 1000

# Initial conditions
y1 = np.array([np.pi/2, 0, np.pi/2, 0])
y2 = np.array([np.pi/2 + 0.001, 0, np.pi/2, 0])  # tiny difference

# Store positions for plotting
positions1 = []
positions2 = []

def get_xy(y):
    """Convert angles to x, y coordinates of the pendulum bobs"""
    theta1, _, theta2, _ = y
    x1 = np.sin(theta1)
    y1 = -np.cos(theta1)
    x2 = x1 + np.sin(theta2)
    y2 = y1 - np.cos(theta2)
    return (x1, y1, x2, y2)

# Precompute positions
for _ in range(steps):
    positions1.append(get_xy(y1))
    positions2.append(get_xy(y2))
    y1 = rk4_step(double_pendulum, y1, 0, dt)
    y2 = rk4_step(double_pendulum, y2, 0, dt)

positions1 = np.array(positions1)
positions2 = np.array(positions2)

# Set up plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2.5, 1)
line1, = ax.plot([], [], 'o-', lw=2, color='blue', label='Trajectory 1')
line2, = ax.plot([], [], 'o-', lw=2, color='red', label='Trajectory 2')
ax.legend()

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

def update(frame):
    x1 = [0, positions1[frame,0], positions1[frame,2]]
    y1 = [0, positions1[frame,1], positions1[frame,3]]
    line1.set_data(x1, y1)

    x2 = [0, positions2[frame,0], positions2[frame,2]]
    y2 = [0, positions2[frame,1], positions2[frame,3]]
    line2.set_data(x2, y2)

    return line1, line2

ani = FuncAnimation(fig, update, frames=steps, init_func=init, blit=True, interval=20)
plt.title("Double Pendulum Chaos Animation")
plt.show()
