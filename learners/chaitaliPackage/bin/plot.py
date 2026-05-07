import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_century_bars(yearly_df):
    summary = (
        yearly_df
        .groupby(["century", "season"])["t_corr"]
        .mean()
        .unstack()
    )

    centuries = summary.index
    seasons = summary.columns

    x = np.arange(len(centuries))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(x - width/2, summary["Summer"], width, label="Summer")
    ax.bar(x + width/2, summary["Winter"], width, label="Winter")

    ax.set_xticks(x)
    ax.set_xticklabels(centuries, rotation=20)
    ax.set_ylabel("Mean temperature (°C)")
    ax.set_title("Uppsala seasonal mean temperature per century")
    ax.legend()

    plt.tight_layout()
    plt.show()