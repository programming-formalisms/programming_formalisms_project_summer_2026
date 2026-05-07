"""Generate figures."""

import matplotlib.pyplot as plt


def create_figure(stats):
    """Plot the stats."""
    print(stats)
    plt.figure()
    plt.plot("Year", "avg_temp", c="red", data=stats.loc[stats["Group"] == 1])
    plt.plot("Year", "avg_temp", c="blue", data=stats.loc[stats["Group"] == 2])
    plt.plot("Year", "avg_temp", c="green", data=stats.loc[stats["Group"] == 3])
    plt.xlabel("Year")
    plt.ylabel("Average Temperature (Summer)")
    plt.title("Weather experiment")
    plt.savefig("figure.png")
    plt.close()


assert create_figure.__doc__
