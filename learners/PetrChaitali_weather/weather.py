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
    if isinstance(df, pd.DataFrame) == True:
        return True
    else:
        return False

def get_seasonal_avg(x):
    """ This function calculates seasonal average.  This function expects  a table with date, time, temperature."""
    if not is_dataframe(x):
        return False
    return True

data = pd.DataFrame.from_dict({'Col1':[1,2,3], 'Col2':[4,5,6]})
assert get_seasonal_avg.__doc__
assert is_dataframe.__doc__
assert table_to_df.__doc__
assert is_dataframe(data)
assert not is_dataframe('oiabroibgao')
assert is_weatherData.__doc__