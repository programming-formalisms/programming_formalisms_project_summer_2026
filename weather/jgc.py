"""Script just reads a file and sotres it in f."""

import os
import pandas as pd

file = "../data/uppsala_tm_1722-2022.txt"
def read_file(your_file):
    """Read a file."""
    with open(your_file) as f:
        f.read()

read_file(file)

data = "../data/uppsala_tm_1722-2022.dat"
dt_clim = pd.read_csv(data)

print(dt_clim)

assert isinstance(statistic,float)

assert isinstance(data,str)
assert os.path.isfile(data)
assert isinstance(dt_clim, pd.DataFrame)
assert os.path.isfile(file)
assert isinstance(file,str)
