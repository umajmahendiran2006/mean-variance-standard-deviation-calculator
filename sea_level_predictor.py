import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Predict from 1880 to 2050
    years = pd.Series(range(1880, 2051))

    plt.plot(
        years,
        slope * years + intercept
    )

    # Line of best fit using data from 2000 onwards
    df_recent = df[df["Year"] >= 2000]

    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    # Predict from 2000 to 2050
    years2 = pd.Series(range(2000, 2051))

    plt.plot(
        years2,
        slope2 * years2 + intercept2
    )

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save and return
    plt.savefig("sea_level_plot.png")
    return plt.gca()
