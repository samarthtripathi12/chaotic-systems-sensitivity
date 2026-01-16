# Chaotic Systems & Sensitivity  
**Project Option 3 – Double Pendulum / Lorenz Attractor**  
*Classical + Nonlinear Physics | Chaos & Sensitivity Analysis*

---

## Overview

This project explores how **deterministic classical systems** can become **unpredictable** due to **exponential sensitivity to initial conditions**. Using the **double pendulum** as a canonical chaotic system, the work demonstrates how even tiny differences in starting conditions lead to dramatically different trajectories, illustrating the core ideas of chaos and limits of prediction.

**Key Highlights:**

- Simulated a double pendulum system using precise RK4 integration.  
- Tested sensitivity to initial conditions by changing angles by `0.001 rad`.  
- Generated **phase-space plots, divergence plots, and animations** to illustrate chaotic behavior.  
- Quantified separation between trajectories to demonstrate **Lyapunov-like exponential growth**.  

---

## Project Layout

chaotic-systems-sensitivity/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│ ├── rk4_solver.py # RK4 numerical integrator
│ ├── test_rk4.py # RK4 validation (Phase 2)
│ ├── double_pendulum.py # Equations of motion (Phase 1)
│ ├── run_double_pendulum.py # Baseline simulation (Phase 3)
│ ├── compute_divergence.py # Sensitivity analysis (Phases 4–5)
│ └── animate_double_pendulum.py # Creates final GIF (Phase 6)
│
├── outputs/
│ ├── phase2_rk4_validation.png # Numerical solver validation
│ ├── phase3_single_chaotic_trajectory.png # Baseline double pendulum
│ ├── phase4_divergence_time_series.png # Δθ vs time showing divergence
│ ├── phase5_phase_space_separation.png # θ vs ω phase-space plot
│ └── phase6_double_pendulum_divergence.gif # Animated trajectories showing chaos
│
└── supplementary/
├── frame_0001.png … frame_0020.png # Optional intermediate frames for verification


> The layout separates **code**, **outputs**, and **supplementary data**, making the project clean and easy to navigate.

---

## Project Phases & Deliverables

### Phase 1 — Physical Model (Foundation)
- Equations of motion for the double pendulum derived from classical mechanics.
- Parameters set: length, mass, gravity.
- Deliverable: Markdown/PDF section explaining the deterministic model.

### Phase 2 — Numerical Solver Validation
- Implemented RK4 solver and validated with a simple pendulum.
- Checked energy conservation and Euler method failure.
- Deliverable: `phase2_rk4_validation.png` showing angle vs time.

### Phase 3 — Baseline Double Pendulum Simulation
- Ran one chaotic trajectory to visualize irregular motion.
- Deliverable: `phase3_single_chaotic_trajectory.png` showing θ1 vs θ2 trajectory.

### Phase 4 — Sensitivity Experiment (Core)
- Simulated two trajectories with Δθ = 0.001.
- Observed divergence over time.
- Deliverables:  
  - `phase4_divergence_time_series.png`  
  - Visual comparison shows trajectories start together then diverge.

### Phase 5 — Quantifying Chaos
- Calculated separation δ(t) between trajectories.
- Plotted ln(δ(t)) vs time to show exponential growth region.
- Deliverable: `phase5_phase_space_separation.png`

### Phase 6 — Limits of Prediction
- Generated animated GIF showing both pendulums swinging together initially, then diverging and moving oppositely.
- Deliverable: `phase6_double_pendulum_divergence.gif`  

> The GIF provides a clear visual demonstration of chaos and divergence over time.

---

## Explanation of Observed Behavior

- Initially, the pendulums follow nearly identical paths.  
- Tiny differences in initial conditions grow exponentially due to **nonlinear dynamics**.  
- Phase-space plots and divergence graphs confirm sensitivity.  
- The system remains deterministic; unpredictability arises from **exponential sensitivity**, not randomness.  

> This is the fundamental principle of chaotic systems: **deterministic laws can produce unpredictable behavior.**

---

## Conclusions

1. **Deterministic systems can be unpredictable:**  
   Small differences in initial conditions lead to large divergences in outcomes.

2. **Numerical methods matter:**  
   RK4 provides stable simulation, while simpler methods like Euler fail over long times.

3. **Visual intuition is powerful:**  
   Phase-space plots and animations communicate chaos clearly.

4. **Limits of prediction are fundamental:**  
   Even with perfect laws, exact future states cannot be predicted beyond a short horizon.

---

## Reproducibility

To reproduce the results, install the required Python packages and run the scripts in sequence:

```bash
# Install dependencies
pip install -r requirements.txt

# Validate RK4 solver
python src/test_rk4.py

# Run baseline simulation
python src/run_double_pendulum.py

# Compute divergence between trajectories
python src/compute_divergence.py

# Animate pendulum motion
python src/animate_double_pendulum.py

All final results will be saved in the outputs/ folder. Intermediate frames, if needed, are in supplementary/.