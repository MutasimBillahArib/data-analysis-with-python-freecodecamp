# 📈 Demographic Data Analyzer

This Python script analyzes demographic data from the U.S. Census Bureau to extract insights related to age, education, income, work hours, nationality, and occupation. It provides a summary of key socioeconomic statistics, particularly focusing on income levels.


## 📊 About the Project

The script processes data from the **Adult Income Dataset** (also known as the "Census Income" dataset) and computes the following:

- Count of each race represented
- Average age of men
- Percentage of people with a Bachelor’s degree
- Percentage of high earners (>50K) with and without advanced education
- Minimum work hours per week and the income distribution among them
- Country with the highest percentage of people earning >50K
- Most common occupation for high earners in India


## 🧪 Example Usage

```python
from demographic_data_analyzer import calculate_demographic_data

results = calculate_demographic_data(print_data=True)
```
This will print a human-readable summary of the results and return them as a dictionary for programmatic use.


## 📐 Features Computed

| Metric                               | Description                                                |
| ------------------------------------ | ---------------------------------------------------------- |
| `race_count`                         | Frequency count of each race                               |
| `average_age_men`                    | Average age of men in the dataset                          |
| `percentage_bachelors`               | Percentage of people with a Bachelor's degree              |
| `higher_education_rich`              | Percentage of people with advanced degrees earning >50K    |
| `lower_education_rich`               | Percentage of people without advanced degrees earning >50K |
| `min_work_hours`                     | Minimum hours worked per week                              |
| `rich_percentage`                    | % of high earners among those who work the fewest hours    |
| `highest_earning_country`            | Country with the highest % of >50K earners                 |
| `highest_earning_country_percentage` | Exact % from the country above                             |
| `top_IN_occupation`                  | Most common occupation among >50K earners in India         |


## 🧠 Learning Outcome

This project is a great introduction to:

- Working with real-world datasets

- Data cleaning and manipulation with `pandas`

- Group-based aggregation and filtering

- Drawing statistical inferences from tabular data


## 👨‍💻 Author

**Mutasim Billah**  

🔗 [LinkedIn](https://www.linkedin.com/in/mmbillah804/)  
🔗 [GitHub](https://github.com/mmbillah804)
