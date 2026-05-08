"""Perform the analysis."""

import os.path

import pandas as pd

from weather.anna import read_data as annas_read_data
from weather.stane import city_dict
from weather.stane import city_filter as peters_city_filter
from weather.sven import create_figure as svens_create_figure
from weather.sven import create_statistics_output as svens_create_statistics_output


def read_data():
    """Read the weather data from file."""
    return annas_read_data()

def city_filter(df: pd.DataFrame, city: str, city_dict=city_dict) -> pd.DataFrame:
    """Filter rows by city using the "city" or the 6th column.

    Valid cities: Uppsala, Risinge, Betna, Linköping, Stockholm, Interpolated.
    Returns a filtered DataFrame.
    """
    return peters_city_filter(df, city, city_dict)

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

# TODO(richelbilderbeek): move these to the 'test' folder # noqa: FIX002
# https://github.com/programming-formalisms/programming_formalisms_project_summer_2026/issues/2

do_analysis()
assert os.path.isfile("figure.png")
assert os.path.isfile("statistics_results.txt")
