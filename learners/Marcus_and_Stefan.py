import os

def file_exists(file_path):
    """
    Check if input file exists
     returns True of file exists, else return False
    """
    # Check if file exists
    return os.path.exists(file_path)
   

def do_experiment():
    """
    Perform experiment
    """
    # Read the data
    # Do the statistics
    # Save the statistics results to file
    assert file_exists("figure.png")
    # Create the figure
    # Save the figure to file
    assert file_exists("statistics_results.txt")

assert do_experiment.__doc__
assert file_exists.__doc__
assert do_experiment()