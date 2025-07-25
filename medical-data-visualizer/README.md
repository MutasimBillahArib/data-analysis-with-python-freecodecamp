# 🩺 Medical Data Visualizer

This project uses Python to analyze and visualize a dataset of medical examination records. It focuses on producing two key visualizations: a categorical plot and a correlation heatmap. These visualizations help reveal insights about cardiovascular disease and related health indicators.


## 📄 Project Overview

This script performs the following:

1. Loads and processes health examination data.
2. Creates a new feature for overweight individuals using BMI.
3. Normalizes the `cholesterol` and `gluc` values for binary classification.
4. Produces:
   - 📊 **Categorical Plot** (`catplot.png`) comparing health indicators grouped by cardiovascular disease.
   - 🔥 **Heat Map** (`heatmap.png`) showing correlations between medical variables.


## 🧪 Example Usage

```python
from medical_data_visualizer import draw_cat_plot, draw_heat_map

draw_cat_plot()
draw_heat_map()
```
The functions will save the plots as `catplot.png` and `heatmap.png` in the current directory.


## ⚙️ Data Preprocessing

### 🧮 Overweight Calculation
A new column `overweight` is calculated using Body Mass Index (BMI):
- Formula: `BMI = weight / (height / 100)^2`
- If BMI > 25 → `overweight = 1`, else `overweight = 0`

### 🔄 Feature Normalization
To simplify analysis:
- `cholesterol` and `gluc` values are normalized to:
  - `0`: normal (original value = 1)
  - `1`: above normal (original value = 2 or 3)

### 🧹 Data Cleaning for Heat Map
- Blood pressure check: `ap_hi` (systolic) should be ≥ `ap_lo` (diastolic)
- Outliers removed using the 2.5th and 97.5th percentiles of:
  - Height
  - Weight


## 📊 Visualizations

### 1. 📑 Categorical Plot (`draw_cat_plot`)
- **Variables plotted:** `cholesterol`, `gluc`, `smoke`, `alco`, `active`, `overweight`
- **Grouped by:** `cardio` (presence or absence of cardiovascular disease)
- **Purpose:** Shows the count of individuals by variable and binary value (0 or 1)

### 2. 🔥 Heat Map (`draw_heat_map`)
- **Displays:** Pearson correlation matrix of medical features
- **Filtered:** Only valid and realistic records (after cleaning)
- **Details:** Includes annotations for each correlation cell for easy interpretation


## 📚 Learning Outcomes

Through this project, you will practice:

- 🧹 **Data cleaning and feature engineering**
- 📊 **Visual storytelling using seaborn and matplotlib**
- 🔍 **Correlation analysis and categorical comparisons**
- 🌐 **Exploring real-world medical datasets with insights**

