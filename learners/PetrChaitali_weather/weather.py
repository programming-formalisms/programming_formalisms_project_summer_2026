# Weather project
import os
import sys
import numpy as np
import pandas as pd

def table_to_df(file):
    """ This function reads in the table. """
    data= pd.read_csv(file)
    return data


def is_dataframe(df):
    """
    Returns true if input is a pd.DataFrame, othewise returns False
    """
    return True

def get_seasonal_avg(x):
    """ This function calculates seasonal average.  This function expects  a table with date, time, temperature."""
    if not is_dataframe(x):
        return False
    return True

assert get_seasonal_avg.__doc__
assert is_dataframe.__doc__
assert table_to_df.__doc__
assert is_dataframe(data)