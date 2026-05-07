def funky(s, filename, num):
    """_summary_

    Args:
        x (_type_): _description_
    """

    f = open(filename, 'w')
    return True


test_filename = 'funky.txt'
assert funky('funky', test_filename, 3)

import os
assert os.path.exists(test_filename)
with open(test_filename) as f:
    lines = f.readlines()
assert len(lines)>0