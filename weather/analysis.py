"""Perform the analysis."""

import os.path

from anna import read_data as annas_read_data
from sven import create_figure as svens_create_figure
from sven import create_statistics_output as svens_create_statistics_output


def check_file_exists(filename:str):
    """Check if file exists. Return True if file exists, false otherwise. Throws TypeError if filename is not a string.

    Args:
        filename (str): path to file

    Returns:
        bool: bool describing file existence
    """
    if not isinstance(filename, str):
        raise TypeError("Input 'filename' expected to be string.")
    if os.path.exists(filename):
        return True
    else:
        return False

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

# TODO(richelbilderbeek): move these to the 'test' folder # noqa: FIX002
# https://github.com/programming-formalisms/programming_formalisms_project_summer_2026/issues/2

do_analysis()
assert os.path.isfile("figure.png")
assert os.path.isfile("statistics_results.txt")
assert check_file_exists('test.txt')

has_thrown = False
try:
    not check_file_exists(1231)
except TypeError as e:
    has_thrown = True
assert has_thrown, "Expected TypeError was not raised"
