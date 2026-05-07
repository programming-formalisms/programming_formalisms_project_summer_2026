"""Extract statistics."""


def extract_stats(data):
    """Extract statistics from data."""
    data = data.loc[(data["Month"] > 5) & (data["Month"] < 9),]
    data = data.loc[data["location"] == 1]
    data.loc[(data["Year"] >= 1750) & (data["Year"] <= 1822), "Group"] = 1
    data.loc[(data["Year"] >= 1850) & (data["Year"] <= 1922), "Group"] = 2
    data.loc[(data["Year"] >= 1950) & (data["Year"] <= 2022), "Group"] = 3
    data = data.groupby(["Year", "Group"]).mean()
    data = data.filter(items=["avg_temp"]).reset_index()
    data.to_csv("statistics_results.txt")
    return data


assert extract_stats.__doc__
