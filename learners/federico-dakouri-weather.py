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


def calculate_stats(data):
    """Calculate statistics from the data."""
    return data


def save_stats_to_file(data, path: Path):
    """Save the statistics to file."""
    with open(path, "w") as outfile:
        outfile.write(data)


def do_experiment():
    # Read the data
    data = read_data(Path("data/uppsala_tm_1722-2022.dat"))
    assert data
    # Do the statistics
    stats = calculate_stats(data)
    assert stats
    # Save the statistics results to file
    save_stats_to_file(stats, Path("statistics_results.txt"))
    assert file_exists(Path("statistics_results.txt"))
    # Create the figure
    # Save the figure to file
    # assert file_exists(Path("statistics_results.txt"))


do_experiment()
