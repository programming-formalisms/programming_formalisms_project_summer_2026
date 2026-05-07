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


test_df = pd.DataFrame.from_dict({'Col1':[1984,1985,1986], 'Col2':[4,5,6], 'Col3':[10,5,26], 'Col4':[10.4,12.7,22.1], 'Col5':[10.1,12.9,21.4],'Col6':[1,2,1]})
test_df_not6 = pd.DataFrame.from_dict({'Col1':[1984,1985,1986], 'Col2':[4,5,6], 'Col3':[10,5,26], 'Col4':[10.4,12.7,22.1],'Col6':[1,2,1]})
def city_filter(df: pd.DataFrame, city: str, city_dict: dict) -> pd.DataFrame:
    """
    Expects a dataframe with 6 columns, where the 6th column represent city/location 
    Valid cities: Uppsala, Risinge, Betna, Linköping, Stockholm, Interpolated
    Returns a dataframe with measurements only from the specified city
    """
    if len(df.columns) != 6:
        raise InvalidColumnCountError(f"The column count is not as expected \nExpected columns count: 6 \nReceived columns: {len(df.columns)}")
    if city not in city_dict.keys():
        raise InvalidCityError(f"City {city} is not defined in the dataset \nDefined cities are: {city_dict.keys()}")
    return True

assert city_filter(test_df, 'Uppsala', city_dict)
