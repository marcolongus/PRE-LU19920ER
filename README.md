# Data and Code for "Spreading processes on heterogeneous active systems: spreading threshold, immunization strategies, and vaccination noise"

This repository contains the datasets and example code corresponding to the article:

**Spreading processes on heterogeneous active systems: spreading threshold, immunization strategies, and vaccination noise**  
*Benjamín Marcolongo, Gustavo J. Sibona, Fernando Peruani*  
Physical Review E (2025)

---

## Repository Structure

- `data/`  
  Plain text files (`.txt`) with the numerical data used to generate each figure panel.  
  Each file has tab-separated columns with a header line.  

- `code/`  
  Example scripts used to generate the figures and perform the simulations.  

---

## Data Files Description

Below is the minimal explanation of each data file and its columns:

- **Fig1_panel_b.txt**  
  - col 1: ⟨v⟩   
  - col 2: ⟨n_R⟩ for single-value distribution  
  - col 3: ⟨n_R⟩ for exponential distribution  
  - col 4: ⟨n_R⟩ for power-law distribution  

- **Fig1_panel_c.txt**  
  - col 1: ⟨v⟩ (average active speed) 
  - col 2: ⟨n_R⟩ (curve single-value distribution)  
  - col 3: ⟨n_R⟩ (curve exponential distribution)  
  - col 4: ⟨n_R⟩ (curve power-law distribution)  

- **Fig1_panel_d.txt**  
  - col 1: ⟨v⟩ (average active speed)
  - col 2: ⟨n_R⟩ (simulation)  
  - col 3: ⟨n_R⟩ (theory)  

- **Fig2_panel_a.txt**  
  - col 1: fraction of vaccinated population (f = N_v / N)  
  - col 2–7: normalized epidemic size for each distribution (single, exponential, power-law, …)  

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
3. To regenerate the figures, run the scripts provided in `code/` (Python ≥ 3.9, NumPy, Matplotlib required).  

---

## Citation

If you use these data or codes, please cite the article:

> B. Marcolongo, G. J. Sibona, and F. Peruani. *Spreading processes on heterogeneous active systems: spreading threshold, immunization strategies, and vaccination noise*. Phys. Rev. E (2025).

---

## License

- **Code**: MIT License (see `LICENSE`)  
- **Data**: CC-BY 4.0 (see `LICENSE_DATA`)  

This means the code can be freely reused and modified with attribution, and the data can be reused provided the original work is cited.
