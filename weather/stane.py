# When done, this should provide all tool to load, preprocess , analyse and visualize Uppsala wetaher data

import numpy as np
import pandas as pd

#--------------------------------------------------
# Custom errors
#--------------------------------------------------
class MyError(Exception):
    """Base class for custom errors"""
    pass
class InvalidCityError(MyError):
    """Raised when city not defined/not part of dataset"""
    pass
class InvalidColumnTypeError(MyError):
    """Raised when column is not present or do not contain expected data type"""
    pass

#--------------------------------------------------
# Helper data
#--------------------------------------------------

# Weather data location
weather_data = "../../data/uppsala_tm_1722-2022.dat"

# City dictionary
city_dict = {
    "Uppsala"           :   1,
    "Risinge"           :   2,
    "Betna"             :   3,
    "Linköping"         :   4,
    "Stockholm"         :   5,
    "Interpolated"      :   6
}

#--------------------------------------------------
# Function definitions
#--------------------------------------------------