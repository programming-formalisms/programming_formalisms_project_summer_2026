"""Perform the analysis."""

import os.path

from modules.io import read_data as io_read_data
from modules.stats import extract_stats
from modules.plot import create_figure as plot_create_figure


def read_data():
    """Read the weather data from file."""
    return io_read_data()


def create_statistics_output(data):
    """Create a file with statistics results."""
    return extract_stats(data)


def create_figure(data):
    """Create the figure for the paper."""
    return plot_create_figure(data)


def do_analysis():
    """Do the analysis."""
    data = read_data()
    create_statistics_output(data)
    create_figure(data)
    print("Analysis done")  # noqa: T201


# TODO(richelbilderbeek): move these to the 'test' folder # noqa: FIX002
# https://github.com/programming-formalisms/programming_formalisms_project_summer_2026/issues/2

do_analysis()
assert os.path.isfile("figure.png")
assert os.path.isfile("statistics_results.txt")
