# Chaotic Systems & Sensitivity  
**Project Option 3 – Double Pendulum / Lorenz Attractor**  
*Classical + Nonlinear Physics | Chaos & Sensitivity Analysis*

---

## Abstract

This project explores how **deterministic classical systems** can produce **unpredictable behavior** due to **exponential sensitivity to initial conditions**, a hallmark of chaos. Using the **double pendulum** as a canonical example, the simulations illustrate how even minute changes in starting conditions lead to dramatically different trajectories.  

The work combines **numerical integration, phase-space analysis, divergence quantification, and animation** to provide an intuitive and visual understanding of chaotic dynamics.

---

## Why This Project

- Provides hands-on demonstration of **chaotic motion** in classical systems.  
- Shows the impact of **tiny changes in initial conditions** on long-term behavior.  
- Highlights the importance of **numerical methods** in accurate simulation.  
- Delivers **visual intuition** through static plots and animated GIFs.  
- Quantifies divergence, showing **Lyapunov-like exponential growth**.  

---

## Development Iterations

- **v1.0:** Baseline double pendulum simulation with RK4 integration  
- **v2.0:** Sensitivity analysis with Δθ = 0.001  
- **v3.0:** Quantification of divergence δ(t) and phase-space plots  
- **v4.0:** Animated GIF showing divergence and limits of predictability  

---

## Verification

- RK4 solver validated against single pendulum trajectories.  
- Divergence of double pendulum trajectories confirmed through plots and animations.  
- Exponential separation region identified, demonstrating Lyapunov-like behavior.

---

## Requirements

- Python 3.11+  
- NumPy  
- Matplotlib  
- (Optional) Numba for speed-up  

---

## Phase 1: Physical Model (Foundation)

**Scientific Question:**  
“What happens to a deterministic system with multiple degrees of freedom?”  

**Description:**  
- Derived equations of motion for the double pendulum from classical mechanics.  
- Set parameters: length, mass, gravity.  
- Establishes a deterministic baseline.  

**Implementation:**  
- Analytical derivation of θ1, θ2 motion equations  
- Baseline simulation setup for RK4 integration  

**End-state / Outputs:**  
- Code: `src/double_pendulum.py`  
- Deliverable: Markdown/PDF explanation of deterministic model  

**What This Proves:**  
- Sets foundation for chaotic dynamics analysis  
- Confirms proper modeling of classical double pendulum  

---

## Phase 2: Numerical Solver Validation

**Scientific Question:**  
“Can my RK4 solver accurately integrate motion?”  

**Implementation:**  
- Tested RK4 solver on simple pendulum  
- Checked energy conservation and identified Euler method failure  

**Static Plot:**  
![Phase 2: RK4 Validation](outputs/phase2_rk4_test.png)  

**End-state / Outputs:**  
- Code: `src/test_rk4.py`  
- Output: `outputs/phase2_rk4_test.png`  

**What This Proves:**  
- RK4 is stable and accurate for double pendulum integration  
- Euler method is inadequate for long-term simulation  

---

## Phase 3: Baseline Double Pendulum Simulation

**Scientific Question:**  
“How does a single double pendulum trajectory behave?”  

**Description:**  
- Ran one trajectory to visualize chaotic motion  
- Observed irregular swinging behavior  

**Static Plot:**  
![Phase 3: Baseline Trajectory](outputs/phase3_double_pendulum_phase_space.png)  

**End-state / Outputs:**  
- Code: `src/run_double_pendulum.py`  
- Output: `outputs/phase3_double_pendulum_phase_space.png`  

**What This Proves:**  
- Demonstrates inherent chaotic motion in the system  
- Provides visual foundation for divergence analysis  

---

## Phase 4: Sensitivity Experiment

**Scientific Question:**  
“How do tiny changes in initial conditions affect motion?”  

**Implementation:**  
- Simulated two trajectories with Δθ = 0.001 rad  
- Observed divergence over time  

**Static Plot:**  
![Phase 4: Divergence](outputs/phase4_output_chaos_divergence.png)  

**End-state / Outputs:**  
- Code: `src/compute_divergence.py`  
- Output: `outputs/phase4_output_chaos_divergence.png`  

**What This Proves:**  
- Tiny initial differences amplify over time  
- Confirms exponential sensitivity characteristic of chaotic systems  

---

## Phase 5: Quantifying Chaos

**Scientific Question:**  
“Can divergence be quantified numerically?”  

**Implementation:**  
- Calculated separation δ(t) between trajectories  
- Plotted ln(δ(t)) vs time to identify exponential growth region  

**Static Plot:**  
![Phase 5: Phase-space & Divergence](outputs/phase5_double_pendulum_swing.png)  

**End-state / Outputs:**  
- Code: `src/compute_divergence.py`  
- Output: `outputs/phase5_double_pendulum_swing.png`  

**What This Proves:**  
- Quantifies Lyapunov-like exponential growth  
- Provides measurable evidence of chaotic dynamics  

---

## Phase 6: Limits of Prediction (Animated Demonstration)

**Scientific Question:**  
“What happens when we visualize divergence over time?”  

**Implementation:**  
- Generated animated GIF showing both pendulums initially moving together  
- Trajectories diverge over time and eventually move oppositely  

**Animated GIF:**  
![Phase 6: Divergence Animation](outputs/phase6_double_pendulum.gif)  

**End-state / Outputs:**  
- Code: `src/animate_double_pendulum.py`  
- Output: `outputs/phase6_double_pendulum.gif`  

**What This Proves:**  
- Provides a **visual demonstration of chaos and prediction limits**  
- Bridges numerical data with intuitive understanding  

---

## Explanation

- Trajectories initially follow nearly identical paths.  
- Tiny differences grow exponentially due to **nonlinear dynamics**.  
- Phase-space and divergence plots confirm sensitivity.  
- System remains deterministic; unpredictability arises from **exponential sensitivity**, not randomness.

---

## Conclusions

1. **Deterministic systems can be unpredictable.**  
   Small differences in initial conditions lead to large divergences.

2. **Numerical methods matter.**  
   RK4 is stable and accurate; simpler methods fail over time.

3. **Visual intuition is powerful.**  
   Phase-space plots and animated GIFs communicate chaos clearly.

4. **Limits of prediction are fundamental.**  
   Exact future states cannot be predicted beyond a short horizon.  

---

## Reproducibility

```bash
# Install dependencies
pip install -r requirements.txt

# Validate RK4 solver
python src/test_rk4.py

# Run baseline double pendulum
python src/run_double_pendulum.py

# Compute divergence
python src/compute_divergence.py

# Animate pendulum motion
python src/animate_double_pendulum.py
