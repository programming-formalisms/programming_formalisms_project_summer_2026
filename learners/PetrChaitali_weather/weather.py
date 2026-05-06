# Weather project
import os
import sys
import numpy as np
import pandas as pd


# column       data
# 1-3          Year, month, day
# 4            Daily average temperature according to observations. 
#                Unit: °C
# 5            Daily average temperatures corrected for the urban effect.
#              NOTE: The urban effects are here updated after 2000 and larger than
#              previously used due to an increased urban heat island at the site.
# 6            Data id no. meaning data from:
#                1=Uppsala, 2=Risinge, 3=Betna, 4=Linköping, 5=Stockholm, 6=Interpolated

def table_to_df(file):
    """ This function reads in the table. """
    data= pd.read_csv(file)
    return data

def is_weatherData(df):
    """
    Tests if columns are as follows: Year[int], Month[int], Day[int], Temperature[float], Temp_corrected[float], Location[int] 1-6

    Returns true if the the format is correct, otherwise returns False (and column name that fails)
    """
    return True

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
assert is_weatherData(test_df)