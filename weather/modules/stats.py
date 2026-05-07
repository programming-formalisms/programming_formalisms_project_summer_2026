"""Extract statistics."""


def extract_stats(data):
    """Extract statistics from data."""
    data = data.loc[(data["Month"] > 5) & (data["Month"] < 9),]
    data = data.loc[data["location"] == 1]
    data = data.groupby("Year").mean()
    return data.filter(items=["avg_temp"])


assert extract_stats.__doc__
