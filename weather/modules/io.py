"""Input/output."""

import re

import pandas as pd
from pathlib import Path


def file_exists(filename: Path):
    """Check if file exists."""
    return filename.is_file()


assert file_exists.__doc__
assert file_exists(Path("../data/uppsala_tm_1722-2022.dat"))
assert not file_exists(Path("file_that_does_not_exist.txt"))


def read_data():
    """Parse the data."""
    filename = Path("../data/uppsala_tm_1722-2022.dat")
    if not file_exists(filename):
        raise RuntimeError("Input file not found or not a valid file!")
    content = []
    with open(filename) as infile:
        for line in infile:
            processed_line = re.sub(r"\s+", " ", line)
            content.append(processed_line.strip().split(" "))

    return pd.DataFrame(
        content,
        columns=["Year", "Month", "Day", "avg_temp", "avg_temp_mod", "location"],
    ).apply(pd.to_numeric)


assert read_data.__doc__
assert not read_data().empty

assert list(read_data().columns) == [
    "Year",
    "Month",
    "Day",
    "avg_temp",
    "avg_temp_mod",
    "location",
]
