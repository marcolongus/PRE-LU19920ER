# Data and Code for "Spreading processes on heterogeneous active systems: spreading threshold, immunization strategies, and vaccination noise"

This repository contains the datasets and example code corresponding to the article:

**Spreading processes on heterogeneous active systems: spreading threshold, immunization strategies, and vaccination noise**  
*Benjamín Marcolongo, Gustavo J. Sibona, Fernando Peruani*  
Physical Review E (2025)

---
## Folder Structure
```text
PRE-LU19920ER/
├── data/                         # TXT files with tab-separated columns
├── code/
│   ├── analysis_and_data/        # analysis scripts + auxiliary data
│   │   ├── scripts/              # python scripts 
│   │   ├── data/ (N=1k,5k,10k)   # intermediate .npy files
│   │   └── images/               # auxiliary figures
│   └── agents_simulation/        # C++ source + headers for simulations
└── README.md
```
---

## Repository Structure

- `data/`  
  Plain text files (`.txt`) with the numerical data used to generate each figure panel.  
  Each file has tab-separated columns with a header line.
```text
├── data/
│   ├── Fig1_panel_b.txt
│   └── Fig1_panel_d.txt
```
- `code/`  
  Example scripts used to generate the figures and perform the simulations.  
```text
├── code/
│   ├── agents_simulation/
│   │   ├── agentes.cpp
│   │   ├── makefile.py
│   │   └── headers/
│   │       ├── agentes.h
│   │       ├── classparticle.h
│   │       └── parameters.h
│   └── analysis_and_data/
│       ├── README_scripts.md
│       ├── fig_txt_geneartor.ipynb
│       ├── data/
│       │   ├── N=1k/ # figures data *.npy
│       │   ├── N=5k/ # figures data *.npy
│       │   └── N=10k/ # figures data *.npy
│       ├── images/ # generated images
│       └── scripts/
│           ├── data_analysis.py
│           ├── pl_exponent_analysis.py
│           └── plot_collapse.py
```
---

## Data Files Description

Below is the minimal explanation of each data file and its columns:

- **Fig1_panel_b.txt**  
  - col 1: ⟨v⟩ (average active speed)   
  - col 2: ⟨n_R⟩ for single-value distribution  
  - col 3: ⟨n_R⟩ for exponential distribution  
  - col 4: ⟨n_R⟩ for power-law distribution  

- **Fig1_panel_c.txt**  
  - col 1: ⟨v⟩ (average active speed same as prev panel.)    
  - col 2: ⟨n_R⟩ for single-value distribution   (calculated directly, see data_analysis.py in code section.) 
  - col 3: ⟨n_R⟩ for exponential distribution   (calculated directly, see data_analysis.py in code section.) 
  - col 4: ⟨n_R⟩ for power-law distribution  (calculated directly, see data_analysis.py in code section.) 

- **Fig1_panel_d.txt**  
  - col 1: q (power law exponent)
  - col 2: ⟨~V⟩^p_c (simulation)  
  - col 3: ⟨~V^p⟩_c (theory) - (calculated directly, see pl_exponent_analysis.py in code section.)  

- **Fig2_panel_a.txt**  
  - col 1: fraction of vaccinated population (f = N_v / N)  
  - col 2–7: normalized epidemic size for each distribution (single, exponential, power-law)  

- **Fig2_panel_b.txt**  
  - col 1: N_v (number of vaccinated agents)  
  - col 2: ⟨n_R⟩ − N_v (epidemic size, single-value distribution)  

- **Fig2_panel_c.txt**  
  - col 1: N_v  
  - col 2: ⟨n_R⟩ − N_v (epidemic size, exponential distribution)  

- **Fig2_panel_d.txt**  
  - col 1: N_v  
  - col 2: ⟨n_R⟩ − N_v (epidemic size, power-law distribution)  

(Insets in the article can be reproduced from these central curves; no extra files are needed.)

---

## How to Use

1. The `.txt` files can be loaded with Python (`pandas.read_csv`), MATLAB, R, or any other data analysis software.  
2. Each file corresponds to one panel of the figures in the article.  
3. To regenerate the figures, run the scripts provided in `code/` (Python ≥ 3.9, NumPy).  

---
## Simulation Details

The raw data in `code/data_and_analysis/data/` (e.g. `N=1k/`, `N=5k/`) were produced using agent-based simulations of **active particles** with heterogeneous speed distributions. The simulations correspond to the scenarios analyzed in the article.

### Model parameters
- **System size (N):** typical runs use *N = 10³* and *N = 5×10³* particles (stored in `N=1k/` and `N=5k/`).
- **Density (ρ):** fixed at ρ = 1000 / 150², so that linear system size *L* varies consistently with *N* to keep ρ constant.
- **Interaction time (τᵢ):** 200.
- **Interaction cross-section (σ):** 4.
- **Composite parameter (Φ):** Φ = 1.4 · ρ · σ · τᵢ, used to determine analytical thresholds.
- **Critical velocities:**  
  - Uniform: v_c = 2 / Φ  
  - Exponential: v_c = 1 / Φ  
  - Power law (q=4): v_c = (3/4) · (2/Φ)

### Speed distributions
Three classes of active speed distributions were simulated:
1. **Single-value (uniform/Dirac)**  
2. **Exponential**  
3. **Power law** with varying exponent q (commonly q = 4, also explored q = 3.1–10).

### Simulation outputs
Each run produces `.npy` arrays containing:
- `velocities_*.npy` → average active speeds ⟨v⟩ (x-axis values).  
- `uniform.npy`, `exponential.npy`, `power_law_alpha=*.npy` → epidemic sizes ⟨n_R⟩ (y-axis values) for the corresponding distribution.  

The **analysis scripts** load these arrays, interpolate them, and compare against theoretical predictions.

### Vaccination strategies
For Fig. 2 in the article:
- **RVS**: Random Vaccination Strategy (uniform random choice of vaccinated agents).  
- **DVS**: Directed Vaccination Strategy (targeted vaccination by activity).  
- Fractions of vaccinated agents *f = N_v / N* are varied (0–30%).  
- Simulation outputs (histograms and average epidemic sizes) are converted into `.txt` files for each panel.

---

### Notes
- The top-level `data/` folder contains the **minimal APS-compliant `.txt` files**, with one file per figure panel.  
- Insets in the article can be reconstructed from the central curves; they are not stored separately.  
- Error bars were omitted in the public `.txt` to simplify reproducibility (as allowed by APS policy).

## Key Parameters

| Symbol | Meaning                         | Value / Expression                 | Notes |
|--------|---------------------------------|------------------------------------|-------|
| **N**  | System size (agents)            | 10³ (`N=1k`) and 5×10³ (`N=5k`)    | Defines the number of active particles |
| **ρ**  | Particle density                | ρ = 1000 / 150²                     | Kept constant while varying N (L scales accordingly) |
| **τᵢ** | Interaction time                | 200                                | Recovery / infection duration |
| **σ**  | Interaction cross-section       | 4                                  | Effective interaction radius |
| **Φ**  | Composite parameter             | Φ = 1.4 · ρ · σ · τᵢ                | Controls epidemic thresholds |
| **v_c (uniform)**     | Critical velocity for single-value distribution | v_c = 2 / Φ       | |
| **v_c (exponential)** | Critical velocity for exponential distribution  | v_c = 1 / Φ       | |
| **v_c (power law)**   | Critical velocity for power-law (q=4)           | v_c = (3/4) · (2/Φ) | General q handled in analysis (`pl_exponent_analysis.py`) |
| **q**  | Power-law exponent               | Typically 4 (also 3.1–10 explored) | Determines heterogeneity of speeds |
| **f**  | Vaccinated fraction              | f = N_v / N (0–0.3 in main figures)| Used for Random (RVS) and Directed (DVS) strategies |


## Citation

If you use these data or codes, please cite the article:

> B. Marcolongo, G. J. Sibona, and F. Peruani. *Spreading processes on heterogeneous active systems: spreading threshold, immunization strategies, and vaccination noise*. Phys. Rev. E (2025).

---

## License

- **Code**: MIT License (see `LICENSE`)  
- **Data**: CC-BY 4.0 (see `LICENSE_DATA`)  

This means the code can be freely reused and modified with attribution, and the data can be reused provided the original work is cited.
