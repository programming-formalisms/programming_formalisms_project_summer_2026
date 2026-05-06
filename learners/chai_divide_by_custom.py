# chai_divide_by.py
import sys

def divide_by(numerator, denominator):
    value = numerator / denominator
    return value

# Get inputs from command line
numerator = float(sys.argv[1])
denominator = float(sys.argv[2])

result = divide_by(numerator, denominator)

print(result)