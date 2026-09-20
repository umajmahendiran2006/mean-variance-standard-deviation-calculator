
import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data
    df = pd.read_csv("adult.data.csv")

    # 1. Count of each race
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )

    # 4. Percentage of people with advanced education
    advanced_education = df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )

    higher_education_rich = round(
        (
            df[advanced_education]["salary"] == ">50K"
        ).mean() * 100,
        1
    )

    # 5. Percentage without advanced education
    lower_education_rich = round(
        (
            df[~advanced_education]["salary"] == ">50K"
        ).mean() * 100,
        1
    )

    # 6. Minimum number of hours worked per week
    min_work_hours = df["hours-per-week"].min()

    # 7. Percentage of people working minimum hours who earn >50K
    min_hours_workers = df[df["hours-per-week"] == min_work_hours]

    num_min_workers = len(min_hours_workers)

    rich_percentage = round(
        (
            min_hours_workers["salary"] == ">50K"
        ).sum() / num_min_workers * 100,
        1
    )

    # 8. Country with highest percentage of people earning >50K
    country_percentage = (
        df.groupby("native-country")["salary"]
        .apply(lambda x: (x == ">50K").mean() * 100)
    )

    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(
        country_percentage.max(), 1
    )

    # 9. Most popular occupation for people earning >50K in India
    india_rich = df[
        (df["native-country"] == "India") &
        (df["salary"] == ">50K")
    ]

    top_IN_occupation = india_rich["occupation"].value_counts().idxmax()

    # Print results
    if print_data:
        print("Number of each race:")
        print(race_count)

        print("Average age of men:")
        print(average_age_men)

        print("Percentage with Bachelors:")
        print(percentage_bachelors)

        print("Percentage with higher education that earn >50K:")
        print(higher_education_rich)

        print("Percentage without higher education that earn >50K:")
        print(lower_education_rich)

        print("Min work time:")
        print(min_work_hours)

        print("Percentage of rich among those who work fewest hours:")
        print(rich_percentage)

        print("Country with highest percentage of rich:")
        print(highest_earning_country)

        print("Percentage of rich in highest earning country:")
        print(highest_earning_country_percentage)

        print("Top occupations in India:")
        print(top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
