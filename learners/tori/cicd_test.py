import os
import pandas as pd
import re


def file_exists(filename):
    """Check if file exists."""
    return os.path.isfile(filename)


def read_data(filename):
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

def extract_stats(content)
    data=pd.DataFrame(columns="year, day, month, avg_temp, avg_temp_fix, location")
    return nothing

assert list(read_data("data/uppsala_tm_1722-2022.dat").columns) == [
    "Year",
    "Month",
    "Day",
    "avg_temp",
    "avg_temp_mod",
    "location",
]


def do_experiment():
    # Read the data
    assert not read_data("data/uppsala_tm_1722-2022.dat").empty
    # Do the statistics
    assert not extract_stats(data).empty
    # Save the statistics results to file
    assert file_exists("statistics_results.txt")
    # Create the figure
    # Save the figure to file
    # assert not file_exists("figure.png")


do_experiment()