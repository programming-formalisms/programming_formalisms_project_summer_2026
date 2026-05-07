"""Generate figures."""

import matplotlib.pyplot as plt


def create_figure(stats):
    """Plot the stats."""
    print(stats)
    plt.figure()
    plt.plot(stats["Year"], stats["avg_temp"], stats["Group"])
    plt.xlabel("Year")
    plt.ylabel("Average Temperature (Summer)")
    plt.title("Weather experiment")
    plt.savefig("figure.png")
    plt.close()


assert create_figure.__doc__
