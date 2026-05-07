"""When done, this module will load, analyse, and visualize Uppsala weather data."""

import pandas as pd


#--------------------------------------------------
# Custom errors
#--------------------------------------------------
class MyError(Exception):

    """Base class for custom errors."""

class InvalidCityError(MyError):

    """Raised when city not defined/not part of dataset."""

class InvalidColumnTypeError(MyError):

    """Raised when column is not present or do not contain expected data type."""

class InvalidColumnCountError(MyError):

    """Raised when column is different than expected."""

#--------------------------------------------------
# Helper data
#--------------------------------------------------

COLUMN_COUNT = 6

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


test_df = pd.DataFrame.from_dict({"Col1":[1984,1985,1986],
                                  "Col2":[4,5,6], "Col3":[10,5,26],
                                  "Col4":[10.4,12.7,22.1],
                                  "Col5":[10.1,12.9,21.4],
                                  "Col6":[1,2,1]})
def city_filter(df: pd.DataFrame, city: str, city_dict: dict) -> pd.DataFrame:
    """Filter rows by city using the 6th column.

    Valid cities: Uppsala, Risinge, Betna, Linköping, Stockholm, Interpolated.
    """
    cities = city_dict.keys()
    col_count = len(df.columns)
    if col_count != COLUMN_COUNT:
        msg = f"Expected 6 columns; Received {col_count}"
        raise InvalidColumnCountError(msg)
    if city not in city_dict:
        msg = f"{city} is not defined, defined cities are: {cities}"
        raise InvalidCityError(msg)
    return True

def yearly_average(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate yearly average temp using the 4th column."""
    
    return True

assert yearly_average(test_df)
