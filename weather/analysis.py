"""Perform the analysis."""

import os.path
from weather.anna import read_data as annas_read_data
from weather.sven import create_figure as svens_create_figure
from weather.sven import create_statistics_output as svens_create_statistics_output


def read_data():
    """Read the weather data from file."""
    return annas_read_data()


def create_figure(data):
    """Create the figure for the paper."""
    return svens_create_figure(data)


def create_statistics_output(data):
    """Create a file with statistics results."""
    return svens_create_statistics_output(data)


def do_analysis():
    """Do the analysis."""
    data = read_data()
    create_statistics_output(data)
    create_figure(data)
    print("Analysis done") # noqa: T201

# TODO: move these to the 'test' folder
do_analysis()
assert os.path.isfile("figure.png")
assert os.path.isfile("statistics_results.txt")
