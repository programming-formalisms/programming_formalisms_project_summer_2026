#import weather

# weather.do_experiment()

def do_experiment(dat_filename):
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

path = "/Users/felixfalk/programming_formalisms_project_summer_2026/data/uppsala_tm_1722-2022.dat"

def read_file(filename):
    import os
    assert os.path.isfile(filename)
    assert os.path.getsize(filename)
    assert os.access(filename, os.R_OK)
    

    file = open(filename, "r")
    content = file.read()

    file.close()
    return content

read_file(path)
