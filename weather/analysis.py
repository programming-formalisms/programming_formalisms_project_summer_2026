"""Perform the analysis."""

from weather.anna import read_data as annas_read_data
fro
def create_statistics_output(data):
    """Create a file with statistics results."""
    return svens_create_statistics_output(data)


def do_analysis():
    """Do the analysis."""
    data = read_data()
    create_statistics_output(data)
    create_figure(data)
    print("Analysis done") # noqa: T201
