# Data and Code for "Spreading processes on heterogeneous active systems: spreading threshold, immunization strategies, and vaccination noise"

This repository contains the datasets and example code corresponding to the article:

**Spreading processes on heterogeneous active systems: spreading threshold, immunization strategies, and vaccination noise**  
*Benjamín Marcolongo, Gustavo J. Sibona, Fernando Peruani*  
Physical Review E (2025) 

---

## Repository Structure

- `data/`  
  Plain text files (`.txt`) with the numerical data used to generate each figure panel.  
  Each file has tab-separated columns with a header line. The correspondence between figures and file names is explained in `readme.txt`.

- `code/`  
  Example scripts used to generate the figures and perform the simulations. These are provided to facilitate reproducibility.  

- `readme.txt`  
  Minimal explanation of each data file, specifying the meaning of each column.  

---

## How to Use

1. The `.txt` files can be loaded directly with Python (`pandas.read_csv`), MATLAB, R, or any other data analysis software.  
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
