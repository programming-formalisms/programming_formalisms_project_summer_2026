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

class MyError(Exception):
    """Base class for custom errors"""
    pass
class InvalidCityError(MyError):
    """Raised when city not defined/not part of dataset"""
    pass
class InvalidColumnTypeError(MyError):
    """Raised when column is not present or do not contain expected data type"""
    pass

weather_data = "../../data/uppsala_tm_1722-2022.dat"

city_dict = {
    "Uppsala"           :   1,
    "Risinge"           :   2,
    "Betna"             :   3,
    "Linköping"         :   4,
    "Stockholm"         :   5,
    "Interpolated"      :   6
}

#input reading
def read_input_file(filename="weather_data.txt"):
    data = pd.read_csv(filename, sep="\t")

    # Check number of columns
    if data.shape[1] != 6:
        print("Weather file must have 6 columns")
        return None, False

    # Expected types for columns 0-5
    expected_types = [
        "int",
        "int",
        "int",
        "float",
        "float",
        "int"
    ]

    for i, expected in enumerate(expected_types):
        col = data.iloc[:, i]

        if expected == "int":
            if not pd.api.types.is_integer_dtype(col):
                raise TypeError(
                    f"Column {i+1} is {col.dtype}. Expected int."
                )

        elif expected == "float":
            if not pd.api.types.is_float_dtype(col):
                raise TypeError(
                    f"Column {i+1} is {col.dtype}. Expected float."
                )

    # Extra validation for last column
    if not data.iloc[:, 5].between(1, 6).all():
        print("Column 6 values must be between 1 and 6.")
        return None, False

    return data, True
    
