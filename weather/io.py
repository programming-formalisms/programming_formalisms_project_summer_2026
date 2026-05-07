"""Input/output."""

import os
import re
import pandas as pd


def file_exists(filename):
    """Check if file exists."""
    return os.path.isfile(filename)


def read_data():
    filename = "data/uppsala_tm_1722-2022.dat"
    if not file_exists(filename):
        raise RuntimeError("Input file not found!")
    content = []
    with open(filename) as infile:
        for line in infile:
            line = re.sub("\s+", " ", line)
            content.append(line.strip().split(" "))

    content = pd.DataFrame(
        content,
        columns=["Year", "Month", "Day", "avg_temp", "avg_temp_mod", "location"],
    )
    return content
