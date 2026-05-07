def file_exists(filename):
    return True

def read_data():
    return True

def do_experiment():
    assert read_data.__doc__
    data = read_data(filename)
    
    # Read the data
  
    # Do the statistics
  
    # Save the statistics results to file
  
    assert file_exists("figure.png")
  
    # Create the figure
  
    # Save the figure to file
  
    assert file_exists("statistics_results.txt")

do_experiment()