from pathlib import Path


def file_exists(path: Path):
    """Check that the file exists."""
    return path.is_file()


assert file_exists(Path("learners/federico-dakouri-weather.py"))
assert not file_exists(Path("figure.png"))


def do_experiment():
    # Read the data
    # Do the statistics
    # Save the statistics results to file
    # assert file_exists(Path("figure.png"))
    # Create the figure
    # Save the figure to file
    # assert file_exists(Path("statistics_results.txt"))
    pass


do_experiment()
