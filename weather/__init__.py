"""Code for the 'weather' package."""
from pathlib import Path

import matplotlib.pyplot as plt


def file_exists(filename):
    return Path(filename).is_file()


def do_experiment():
    # Save the statistics results to file
    with open("statistics_results.txt", "w") as file:
        file.write("Statistics results\n")
        file.write("Mean: 0\n")
        file.write("Standard deviation: 0\n")

    assert file_exists("statistics_results.txt")

    # Create and save the figure
    plt.figure()
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Weather experiment")
    plt.savefig("figure.png")
    plt.close()

    assert file_exists("figure.png")
