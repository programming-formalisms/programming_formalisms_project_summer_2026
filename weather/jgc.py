import os

file = "../data/uppsala_tm_1722-2022.txt"

with open(file) as f:
    print(f.read())

#assert os._exists(file) # This does not work but is not giving error!
assert isinstance(file,str)
