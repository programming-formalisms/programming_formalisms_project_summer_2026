import os
import pandas as pd


def file_exists(filename):
    """Check if file exists."""
    return os.path.isfile(filename)

def read_data(filename):
    content = pd.read_csv(filename, sep='\t')
    assert column_names == 'Year, Month, Day, avg_temp, avg_temp_mod, location'
    return content

def do_experiment():
    # Read the data
    assert not read_data("data/uppsala_tm_1722-2022.dat").empty
    # Do the statistics
    # Save the statistics results to file
    assert file_exists("statistics_results.txt")
    # Create the figure
    # Save the figure to file
    assert not file_exists("figure.png")


do_experiment()
