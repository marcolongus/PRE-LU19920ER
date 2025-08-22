# Scripts

This folder contains the Python scripts used for analysis and figure generation in the article
**"Spreading processes on heterogeneous active systems: spreading threshold, immunization strategies, and vaccination noise"**.

---

## Usage Notes

- Run all scripts **from the root of the repository** so that relative paths to `data/` and `images/` work correctly.
- Python ≥ 3.9 is recommended.
- Dependencies: `numpy`, `matplotlib`, `scipy`.

Example:

```bash
cd /path/to/repo/code/analysis_and_data/scripts
python data_analysis.py
```

## Scripts Overview

### `data_analysis.py`
- Loads `.npy` simulation data from `data/N=1k` (and optionally `data/N=5k`).  
- Plots outbreak size ⟨n_R⟩ vs average speed ⟨v⟩ for different speed distributions (uniform, exponential, power-law).  
- Compares simulations with theoretical predictions.  
- **Outputs:**  
  - `images/n_R_simulation.png`  
  - `images/n_R_theory.png`

---

### `pl_exponent_analysis.py`
- Analyzes how the epidemic threshold depends on the power-law exponent `q`.  
- Loads multiple simulation files with different `q` values.  
- Detects critical velocities and compares with theoretical results.  
- **Outputs:**  
  - `images/q-curves-end.png`  
  - `images/p_comparison.png`

---

### `plot_collapse.py`
- Produces scaling plots by normalizing ⟨v⟩ with ⟨v²⟩.  
- Shows collapse of simulation results across different distributions.  
- Adds theoretical predictions for comparison.  
- **Outputs:**  
  - `images/simulations_vsaquare_v.png`  
  - `images/theory_vsquare_v.png`
