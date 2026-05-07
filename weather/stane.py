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
### default file
weather_data = "../../data/uppsala_tm_1722-2022.dat"


def file_is_tsv(file):
    """Checks if file exists and is readable as TSV."""
    try:
        data = pd.read_csv(file, sep="\t")
        return data
    except Exception as e:
        print(f"Invalid TSV file: {e}")
        return None


def load_data(path: str) -> pd.DataFrame:
    """Reads a TSV file and returns a dataframe."""
    return pd.read_table(path)


def weather_data(filename):
    """Validates weather data format."""
    
    data = file_is_tsv(filename)

    if data is None:
        return None, False

    # Check number of columns
    if data.shape[1] != 6:
        print("Weather file must have 6 columns")
        return None, False

    # Expected types
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

    # Check final column values
    if not data.iloc[:, 5].between(1, 6).all():
        print("Column 6 values must be between 1 and 6.")
        return None, False
    print(data.head())
    return data, True


