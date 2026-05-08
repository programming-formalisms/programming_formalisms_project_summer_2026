"""Perform the analysis."""

import os
import pandas as pd

from weather.anna import read_data as annas_read_data
from weather.sven import create_figure as svens_create_figure
from weather.sven import create_statistics_output as svens_create_statistics_output




def read_data(file_path):

    """
    Read the data into a dataframe
    """
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"error")

    column_names = [
        'year', 'month', 'day', 
        'avg_temp', 'corrected_temp', 'location_id'
    ]


    df = pd.read_csv(file_path, sep=r'\s+', names=column_names)
    
    assert not df.empty, "error"
    assert len(df.columns) == 6, f"error"

    return df


def create_figure(data):
    """Create the figure for the paper."""
    return svens_create_figure(data)


def create_statistics_output(data):
    """Create a file with statistics results."""
    return svens_create_statistics_output(data)


def do_analysis(file_path):
    """Do the analysis."""
    data = read_data(file_path)
    create_statistics_output(data)
    create_figure(data)
    print("Analysis done") # noqa: T201

# TODO(richelbilderbeek): move these to the 'test' folder # noqa: FIX002
# https://github.com/programming-formalisms/programming_formalisms_project_summer_2026/issues/2


path = r"data\uppsala_tm_1722-2022.dat"  
do_analysis(path)
assert os.path.isfile("figure.png")
assert os.path.isfile("statistics_results.txt")

data = read_data(path)