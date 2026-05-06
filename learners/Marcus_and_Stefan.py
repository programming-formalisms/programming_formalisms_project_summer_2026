def file_exists(file_path):
    """
    Check if input file exists
    """
    # Check if file exists
    pass

def do_experiment():
    # Read the data
    # Do the statistics
    # Save the statistics results to file
    assert file_exists("figure.png")
    # Create the figure
    # Save the figure to file
    assert file_exists("statistics_results.txt")

assert do_experiment.__doc__
assert file_exists.__doc__