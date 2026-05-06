import os


def file_exists(filename):
    """Check if file exists."""
    return os.path.isfile(filename)


def do_experiment():
    # Read the data
    assert read_data("data/uppsala_tm_1722-2022.dat")
    # Do the statistics
    # Save the statistics results to file
    assert file_exists("statistics_results.txt")
    # Create the figure
    # Save the figure to file
    assert not file_exists("figure.png")


do_experiment()
