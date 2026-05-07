def divide_by(numerator, denominator):
    assert denominator != 0
    assert isinstance(numerator, (float,int))
    assert isinstance(denominator, (float,int))
    return (numerator / denominator)

print(divide_by(3.0,2))


def read_file(filename):
    import os
    assert os.path.isfile(filename)
    assert os.access(filename, os.R_OK)
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

print(read_file("/home/tori-giffin/repos/programming_formalisms_project_summer_2026/learners/tori/fairytale.md"))

def read_non_empty_file(filename):
    import os
    assert os.path.isfile(filename)
    assert os.access(filename, os.R_OK)
    file = open(filename, "r")
    content = file.read()
    if len(content) == 0:      
        raise ValueError("File has no content")
    file.close()
    return content

print(read_non_empty_file("/home/tori-giffin/repos/programming_formalisms_project_summer_2026/learners/tori/empty_file.txt"))

    ##Exercise 5
    import weather
    weather.do_experiment(filename)
        import os
        assert os.path.isfile(filename)
        assert os.access(filename, os.R_OK)
        #read the data
        #do the statistics
        #save the statistics results to file
        assert os.path.isfile("statistics_results.txt")
        #create the figure 
        #save the figure to file
        assert os.path.isfile("figure")
    