def read_file(filename):
    #import os
    #assert os.path.isfile(filename)
    #assert os.access(filename, os.R_OK)

    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

#read_file('haea.txt')

def read_non_empty_file(filename):
    import os
    assert os.path.isfile(filename)
    assert os.access(filename, os.R_OK)
    file = open(filename, "r")
    content = file.read()
    # file is not empty
    assert len(content) > 0
    file.close()
    return content

read_non_empty_file('learners/eva/test.txt')

