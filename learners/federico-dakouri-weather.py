from pathlib import Path


def file_exists(path: Path):
    """Check that the file exists."""
    return path.is_file()


assert file_exists(Path("data/uppsala_tm_1722-2022.dat"))
assert not file_exists(Path("file_that_does_not_exist.txt"))


def read_data(path: Path):
    """Parse the input file."""
    with open(path) as infile:
        data = infile.read()
    return data


assert read_data(Path("data/uppsala_tm_1722-2022.dat"))


def calculate_stats(data):
    """Calculate statistics from the data."""
    Path("statistics_results.txt").touch()


data = read_data(Path("data/uppsala_tm_1722-2022.dat"))
calculate_stats(data)

assert file_exists(Path("statistics_results.txt"))


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
