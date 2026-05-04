"""Sven's code."""


def create_figure(unused_data):  # noqa: ARG001
    """Create the figure for the paper."""
    open("figure.png", "a").close()  # Create the file if it does not exist
    with open("figure.png", "w") as figure_file:
        figure_file.write("Stub for an image")
    print("Sven's function has created a figure") # noqa: T021


def create_statistics_output(unused_data):  # noqa: ARG001
    """Create a file with statistics results."""
    open("statistics_results.txt", "a").close()  # Create the file if it does not exist
    with open("statistics_results.txt", "w") as stats_file:
        stats_file.write("Stub for a statistics file")
    print("Sven's function has created statistics output") # noqa: T021
