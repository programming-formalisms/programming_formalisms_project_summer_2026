# The last commit passed all the things so we will break it by adding this very large stupid line and breaking the assert 
import os

file = "../data/uppsala_tm_1722-2022.txt"

with open(file) as f:
    print(f.read())

assert os._exists(file) # This does not work but is not giving error!
assert type(file) == str 
