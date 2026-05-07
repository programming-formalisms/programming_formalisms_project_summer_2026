import os

def file_exists(filename):
    return True

def read_data(datatxtfile):
    """
    Reading data from a text file! 
    """
    if os.path.isfile(datatxtfile):
        return True
read_data('t1.txt')

def do_experiment():
    
    # Read the data
    assert read_data.__doc__
    data = read_data(datatxtfile)
    
    # Do the statistics
  
    # Save the statistics results to file
  
    assert file_exists("figure.png")
  
    # Create the figure
  
    # Save the figure to file
  
    assert file_exists("statistics_results.txt")

do_experiment()