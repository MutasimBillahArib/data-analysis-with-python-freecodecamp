import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    total_bachelors = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round((total_bachelors / df.shape[0]) * 100, 1)

    # Advanced education filter
    advanced_degrees = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(advanced_degrees)]
    lower_education = df[~df['education'].isin(advanced_degrees)]

    # Percentage of advanced education holders earning >50K
    higher_rich = higher_education[higher_education['salary'] == '>50K'].shape[0]
    higher_education_rich = round((higher_rich / higher_education.shape[0]) * 100, 1)

    # Percentage of non-advanced education holders earning >50K
    lower_rich = lower_education[lower_education['salary'] == '>50K'].shape[0]
    lower_education_rich = round((lower_rich / lower_education.shape[0]) * 100, 1)

    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # Number of people who work the minimum number of hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    # Percentage of rich among those who work the minimum number of hours
    rich_min_workers = num_min_workers[num_min_workers['salary'] == '>50K'].shape[0]
    rich_percentage = round((rich_min_workers / num_min_workers.shape[0]) * 100, 1)

    # Country with highest percentage earning >50K
    country_groups = df.groupby('native-country')
    country_rich_percentage = (country_groups['salary'].apply(lambda x: (x == '>50K').mean() * 100).round(1))
    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = country_rich_percentage.max()

    # Most popular occupation for those earning >50K in India
    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_earners['occupation'].mode()[0] if not india_high_earners.empty else None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
