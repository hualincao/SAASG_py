# SAASG-MS-TWDTW

A Multi-Source Time-Weighted Dynamic Time Warping framework for large-scale crop mapping with spatial transfer.

---

## 📌 Overview

This repository provides the implementation of a **multi-source phenology-based crop mapping framework**, including:

* Standard Multi-Phase Feature Curve (S-MPFC) construction
* Multi-Source Time-Weighted Dynamic Time Warping (MS-TWDTW)
* Grid-based spatial transfer with iterative sample generation

The framework integrates **Sentinel-1 SAR + Sentinel-2 optical features (NDVI, CNDVI)** to improve crop discrimination under spatial heterogeneity.

---

## 📁 Project Structure

```
SAASG/
├── gee/
│   ├── data_preprocess.py        # Sentinel-1 / Sentinel-2 data preprocessing
│   └── feature_extraction.py     # NDVI, CNDVI, SAR feature construction
│
├── python/
│   ├── 01_build_smpfc.py         # Construct standard phenological feature curves
│   ├── 02_ms_twdtw.py            # Multi-source TWDTW implementation
│   ├── 03_grid_transfer.py       # Spatial transfer & sample propagation
│
├── data/
│   ├── 2024_调研点_整理.shp.shp                # Training / validation sample points (Shapefile)
│   ├── 2024_调研点_整理.shp.dbf
│   ├── 2024_调研点_整理.shp.shx
│   ├── 2024_调研点_整理.shp.prj
│   └── 2024_调研点_整理.shp.cpg
│
├── results/                      # Output results (curves, maps, samples)
├── requirements.txt
└── README.md
```

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Main dependencies:

* earthengine-api
* geemap
* numpy
* scipy
* scikit-learn
* tqdm

---

## 🌍 Google Earth Engine Setup

```bash
earthengine authenticate
```

Then initialize in Python:

```python
import ee
ee.Initialize()
```

---

## 🚀 Usage

### 1️⃣ Build Standard Phenological Curve

```bash
python python/01_build_smpfc.py
```

Output:

```
results/mean_curve.npy
results/time.npy
```

---

### 2️⃣ Run MS-TWDTW

```bash
python python/02_ms_twdtw.py
```

---

### 3️⃣ Grid-based Spatial Transfer

```bash
python python/03_grid_transfer.py
```

---

## 📊 Features Used

| Feature | Description                  |
| ------- | ---------------------------- |
| SAR     | VV + VH                      |
| NDVI    | (B8 - B4) / (B8 + B4)        |
| CNDVI   | NDVI with texture constraint |

---

## 🧠 Method Highlights

* Multi-phase feature fusion (SAR → NDVI → CNDVI)
* Time-weighted DTW with phenological constraints
* 8-neighbor spatial transfer strategy
* Iterative sample generation across grids

---

## 📄 Citation

If you use this code, please cite:

```
A Spatially-Adaptive Automated Sample Generation Framework via Multi-Source Phenological Fusion for Large-Scale Crop Mapping: Demonstrated on Peanuts in Shandong, China
```

---

## 📬 Contact

For questions, please contact:

* Author: Hualin Cao
* Email: 2176518050@qq.com

---
