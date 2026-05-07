"""When done, this module will load, analyse, and visualize Uppsala weather data."""

import pandas as pd
import os

#--------------------------------------------------
# Custom errors
#--------------------------------------------------
class MyError(Exception):

    """Base class for custom errors."""

class InvalidCityError(MyError):

    """Raised when city not defined/not part of dataset."""

class InvalidColumnTypeError(MyError):

    """Raised when column is not present or do not contain expected data type."""


#--------------------------------------------------
# Helper data
#--------------------------------------------------

# Weather data location
weather_data = "../data/uppsala_tm_1722-2022.dat"

# City dictionary
city_dict = {
    "Uppsala"           :   1,
    "Risinge"           :   2,
    "Betna"             :   3,
    "Linköping"         :   4,
    "Stockholm"         :   5,
    "Interpolated"      :   6,
}

#--------------------------------------------------
# Function definitions
#--------------------------------------------------

def file_is_tsv():
    """Checks if file exists and if it is a valid tsv format"""
def load_data(path: str) -> pd.DataFrame:
    """This function reads in the table and returns a dataframe."""
    pd.read_table(path)