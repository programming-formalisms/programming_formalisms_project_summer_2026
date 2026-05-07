"""Analysis of weather data. Takes average temps and creates a stats file and figure."""

import os
import pandas as pd
import re
from scipy import stats


def file_exists(filename):
    """Check if file exists."""
    return os.path.isfile(filename)


def read_data(filename):
    """Reads file into data frame."""
    content = []
    with open(filename) as infile:
        for line in infile:
            line = re.sub("[ ]+", " ", line)
            content.append(line.strip().split(" "))

    content = pd.DataFrame(
        content,
        columns=["Year", "Month", "Day", "avg_temp", "avg_temp_mod", "location"],
    )
    return content

def extract_stats(content):
    """Extracts the average from the data frame."""
    mean_data = content.astype(float).mean()
    return mean_data

def get_regression(content):
    """Does a linear regression of the data and outputs a p-value."""
    content = content.astype(float)
    x, y = content['Year'], content['avg_temp_mod']
    statistic = slope, intercept, r, p, std_err = stats.linregress(x,y)
    
    return statistic.pvalue

assert list(read_data("data/uppsala_tm_1722-2022.dat").columns) == [
    "Year",
    "Month",
    "Day",
    "avg_temp",
    "avg_temp_mod",
    "location",
]


def do_experiment(file):
    # Read the data
    file_exists(file)
    content = read_data(file)
    assert not content.empty
    # Do the statistics
    data = extract_stats(content)
    assert not data.empty
    statistic = get_regression(content)
    assert isinstance(statistic, float)
    # Save the statistics results to file
    assert file_exists("statistics_results.txt")
    # Create the figure
    # Save the figure to file
    # assert not file_exists("figure.png")


do_experiment("data/uppsala_tm_1722-2022.dat")