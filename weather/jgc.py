""" This script just reads a file and sotres it in f"""

import os
import typing

file = "../data/uppsala_tm_1722-2022.txt"
def read_file(your_file):
    with open(your_file) as f:
        f.read()
        
read_file(file)

assert os.path.isfile(file)
assert isinstance(file,str)
