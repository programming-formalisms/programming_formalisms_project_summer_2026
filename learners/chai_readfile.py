def read_file(filename):
    #This function assumes that the file is in the current directory
    #This function assumes that this file is readable.
    import os
    assert os.path.isfile(filename)
    assert os.access(filename, os.R_OK)
    file = open(filename)
    content = file.read()
    file.close()
    return content


def read_non_empty_file(filename):
    import os
    assert os.path.isfile(filename)
    assert os.access(filename, os.R_OK)
    file = open(filename)
    content = file.read()
    file.close()
    return content
