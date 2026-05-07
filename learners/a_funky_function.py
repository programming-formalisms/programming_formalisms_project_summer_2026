def funky(s, filename, num):
    """_summary_

    Args:
        x (_type_): _description_
    """

    f = open(filename, 'w')
    f.write(s)
    f.close()

    return True


test_filename = 'funky.txt'
test_string = 'funky'
test_num = 3
assert funky(test_string, test_filename, test_num)

import os
assert os.path.exists(test_filename)
with open(test_filename) as f:
    lines = f.readlines()

assert len(lines)>0

assert test_string in lines[0]
print(lines)

assert len(lines)==test_num
