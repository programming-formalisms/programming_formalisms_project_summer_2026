"""Perform the analysis."""


def do_analysis():
    """Do the analysis."""
    open("figure.png", "a").close() # Create the file if it does not exist
    with open("figure.png", "w") as figure_file:
        figure_file.write("Stub for an image")

    open("statistics_results.txt", "a").close() # Create the file if it does not exist
    with open("statistics_results.txt", "w") as stats_file:
        stats_file.write("Stub for a statistics file")
