# 🌊 Sea Level Predictor

This project visualizes historical sea level data and uses linear regression to predict future trends. The script generates a scatter plot of measured sea level data, along with two lines of best fit — one for the full dataset and another starting from the year 2000 — to model the rise in sea level over time.


## 📊 Visualization

The output plot `sea_level_plot.png` includes:
- **Blue dots**: Historical sea level measurements from 1880 to present
- **Red line**: Linear regression line using **all data** (1880–present)
- **Green line**: Linear regression line using **recent data** (from 2000 onward)
- **X-axis**: Year (1880–2050)
- **Y-axis**: Sea Level (inches)
- **Title**: *"Rise in Sea Level"*


## 🧠 What It Shows

- How sea level has changed over time
- Projected sea level rise if current trends continue
- Visual comparison between long-term and recent trends


## 🧪 Example Usage

```python
from sea_level_predictor import draw_plot

draw_plot()
```

This will:

- 📈 Create and save the visualization as `sea_level_plot.png`
- 🧩 Return the current `matplotlib` axes object for optional further manipulation or integration


## 📚 Learning Objectives

Through this project, you’ll practice:

- 🌍 Loading and analyzing real-world environmental data
- 📉 Applying linear regression using `scipy.stats.linregress`
- 📈 Predictive modeling and extrapolation to future years
- 🎨 Custom plotting and styling using `matplotlib`

