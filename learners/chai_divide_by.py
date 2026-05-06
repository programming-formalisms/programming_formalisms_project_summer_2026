#divide script
import os
import sys

def divide_by_3(numerator, denominator):
    assert isinstance(numerator, (float, int))
    assert isinstance(denominator, (float, int))
    assert type(numerator) == type(denominator)
    assert(denominator != 0.0)
    value = numerator / denominator
    return(value)

numerator = float(sys.argv[1])
denominator =float(sys.argv[2])
result = divide_by_3(numerator, denominator) #running the function to get values
print(result) #printing results on screen
