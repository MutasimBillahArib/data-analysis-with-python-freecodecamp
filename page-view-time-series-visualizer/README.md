# 📈 Page View Time Series Visualizer

This project uses Python to explore and visualize time series data of daily page views on the freeCodeCamp Forum. The script generates three informative visualizations: a line plot, a bar plot, and box plots to reveal trends, seasonality, and distribution of forum activity over time.


## 📄 Dataset

- **File Required:** `fcc-forum-pageviews.csv`
- **Columns:**
  - `date`: Date of page view
  - `value`: Number of page views on that day
- **Source:** freeCodeCamp Forum activity (May 2016 - December 2019)


## 📊 Visualizations

### 1. Line Plot (`draw_line_plot`)
Displays daily page views over time to show overall trends.

- **File saved as:** `line_plot.png`
- **Features:**
  - Red line for daily views
  - Clean X and Y axis labels
  - Title with time span: _"Daily freeCodeCamp Forum Page Views 5/2016-12/2019"_


### 2. Bar Plot (`draw_bar_plot`)
Displays average monthly page views grouped by year.

- **File saved as:** `bar_plot.png`
- **Features:**
  - X-axis: Years
  - Y-axis: Average page views
  - Colored bars by month
  - Full month names in proper calendar order


### 3. Box Plots (`draw_box_plot`)
Displays distributions to reveal:
- **Year-wise trends**
- **Month-wise seasonality**

- **File saved as:** `box_plot.png`
- **Features:**
  - Two side-by-side box plots
  - Month-wise box plot uses 3-letter abbreviations (`Jan`, `Feb`, ..., `Dec`)


## 🧹 Data Cleaning

Before plotting:
- Outliers removed using 2.5th and 97.5th percentiles
- Dates parsed and set as DataFrame index
- Month/Year columns extracted for grouping


## 📚 Learning Objectives

This project demonstrates:

- Time series analysis using `pandas`

- Grouping and aggregation by time periods

- Outlier detection and removal

- Use of seaborn and matplotlib for custom plots

- Clear, interpretable data visualization practices


## 👨‍💻 Author

**Mutasim Billah**  

🔗 [LinkedIn](https://www.linkedin.com/in/mmbillah804/)  
🔗 [GitHub](https://github.com/mmbillah804)
