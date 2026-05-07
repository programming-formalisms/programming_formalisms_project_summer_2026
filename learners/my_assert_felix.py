#def divide_by(numerator, denominator):
#    assert denominator != 0.0
#    assert isinstance(numerator, float)
#    assert isinstance(denominator, float)
#    return (numerator / denominator)

#divide_by(3, 4)

def read_file(filename):
    import os
    assert os.path.isfile(filename)
    assert os.access(filename, os.R_OK)

    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

read_file("/Users/felix.falk/programming_formalisms_project_summer_2026/learners/fairytale_felix_claudia.md")

print(read_file("/Users/felix.falk/programming_formalisms_project_summer_2026/learners/fairytale_felix_claudia.md"))

read_file("/Users/felix.falk/programming_formalisms_project_summer_2026/learners/fqwgqgwqggqe.md") 

def read_non_empty_file(filename):
    import os
    assert os.path.isfile(filename)
    assert os.access(filename, os.R_OK)
    
    file = open(filename, "r")
    content = file.read()
    
    assert content != NULL

    file.close()
    return content

import weather
import os
assert os.path.isfile(filename) # Is the filename correct? 
assert os.access(filename, os.R_OK) # Is the file readable?

weather.do_experiment()

def do_experiment():
    import os
    assert os.path.isfile(filename) # Is the filename correct? 
    assert os.access(filename, os.R_OK) # Is the file readable?
  # Read the data
    # Assert that the correct columns are in the file
    assert isinstance(numerator, float) # Assert that the data is correctly formatted
  # Do the statistics
    # Assert that statistics have been created
  # Save the statistics results to file
  # Create the figure
  # Save the figure to file
    assert file_exists("figure.png") # Is the output figure created? 
    assert file_exists("statistics.txt") # Is the output statistic file created? 
