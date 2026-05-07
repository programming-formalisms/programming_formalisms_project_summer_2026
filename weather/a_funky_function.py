"""A module to create a file with n number of repetitions of a string s."""

import os


def funky(s:str, filename:str, num:int):
    """Make file with string s number (num) of times.

    Args:
        s (str): _description_
        filename (str): _description_
        num (int): _description_

    Returns:
        _type_: _description_

    """
    with open(filename, "w") as f:
        for _i in range(num):
            f.writelines(s+"\n")

    return True

test_filename = "funky.txt"
test_string = "funky"
test_num = 3
assert funky(test_string, test_filename, test_num)


assert os.path.exists(test_filename)
with open(test_filename) as f:
    lines = f.readlines()

assert len(lines)>0

assert test_string in lines[0]

assert len(lines)==test_num
