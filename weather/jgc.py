import os

file = "../data/uppsala_tm_1722-2022.txt"

with open(file) as f:
    print(f.read())

assert os.path.isfile(file)
assert isinstance(file,str)
