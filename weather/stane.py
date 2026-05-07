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

INPUT_COLUMN_COUNT = 6
OUTPUT_COLUMN_COUNT = 3

COL_NAMES=["year","month","day","temp","temp2","city"]

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


def file_is_fwf(file):
    """Check if file exists and is readable as fwf."""
    try:
        return pd.read_fwf(file)
    except pd.errors.DataError: #Needs to be tested
        return None

def load_data(path: str) -> pd.DataFrame:
    """Read a TSV file and returns a dataframe."""
    return pd.read_fwf(path)


def validate_input_data_format(filename):
    """Validate weather data format."""
    data = file_is_fwf(filename)

    if data is None:
        return None, False

    # Check number of columns
    if data.shape[1] != INPUT_COLUMN_COUNT:
        return None, False

    # Expected types
    expected_types = [
        "int",
        "int",
        "int",
        "float",
        "float",
        "int",
    ]

    for i, expected in enumerate(expected_types):
        col = data.iloc[:, i]

        if expected == "int":
            if not pd.api.types.is_integer_dtype(col):
                msg = f"Column {i+1} is {col.dtype}. Expected int."
                raise TypeError(
                    msg,
                )

        elif expected == "float" and not pd.api.types.is_float_dtype(col):
            msg_0 = f"Column {i+1} is {col.dtype}. Expected float."
            raise TypeError(
                msg_0,
            )

    # Check final column values
    if not data.iloc[:, 5].between(1, 6).all():
        return None, False
    return data, True


#output function


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
    if col_count != INPUT_COLUMN_COUNT:
        msg = f"Expected 6 columns; Received {col_count}"
        raise InvalidColumnCountError(msg)
    if city not in city_dict:
        msg = f"{city} is not defined, defined cities are: {cities}"
        raise InvalidCityError(msg)
    if "city" not in df.columns:
#       Warning, city not detected in df, resolving cols by order
        return df[df.iloc[:, 5] == city_dict[city]]
    return df[df["city"] == city_dict[city]]

def yearly_average_temp(df: pd.DataFrame) -> pd.Series:
    """Calculate yearly average temp using the 4th column."""
    if "year" not in df.columns or "temp" not in df.columns:
#       Warning, year or temp not detected in df, resolving cols by order
        return df.groupby(df.iloc[:, 0]).mean().iloc[:, 3]
    return df.groupby("year").mean()["temp"]

def read_output(df):
    """Validate output dataframe format."""
    # Check input is actually a DataFrame
    if not isinstance(df, pd.DataFrame):
        return None, False

    # Check number of columns
    if df.shape[1] != OUTPUT_COLUMN_COUNT:
        return None, False

    # Expected column types
    expected_types = [
        "int",
        "float",
    ]

    for i, expected in enumerate(expected_types):
        col = df.iloc[:, i]

        if expected == "int":
            if not pd.api.types.is_integer_dtype(col):
                msg = f"Column {i+1} is {col.dtype}. Expected int."
                raise TypeError(
                    msg,
                )

        elif expected == "float" and not pd.api.types.is_float_dtype(col):
            msg_0 = f"Column {i+1} is {col.dtype}. Expected float."
            raise TypeError(
                msg_0,
            )

    return df, True


def write_output(df, filename="output.csv"):
    """Write dataframe to CSV file."""
    if not isinstance(df, pd.DataFrame):
        return False

    df.to_csv(filename, index=False)

    return True

