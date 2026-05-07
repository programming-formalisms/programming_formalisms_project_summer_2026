def funky(s, filename, num):
    """_summary_

    Args:
        x (_type_): _description_
    """

    f = open(filename, 'w')
    f.write('blub')
    f.close()

    return True


test_filename = 'funky.txt'
test_string = 'funky'
assert funky(test_string, test_filename, 3)

import os
assert os.path.exists(test_filename)
with open(test_filename) as f:
    lines = f.readlines()

assert len(lines)>0

assert test_string in lines[0]