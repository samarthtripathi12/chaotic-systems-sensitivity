import numpy as np

def rk4_step(f, y, t, dt):
    """
    One step of 4th-order Runge-Kutta integration
    """
    k1 = f(y, t)
    k2 = f(y + 0.5 * dt * k1, t + 0.5 * dt)
    k3 = f(y + 0.5 * dt * k2, t + 0.5 * dt)
    k4 = f(y + dt * k3, t + dt)
    return y + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
