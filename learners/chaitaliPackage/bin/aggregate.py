import pandas as pd

CENTURIES = {
    "1722–1821": (1722, 1821),
    "1822–1921": (1822, 1921),
    "1922–2022": (1922, 2022),
}

def assign_century(year):
    for name, (start, end) in CENTURIES.items():
        if start <= year <= end:
            return name
    return None

def assign_season(month):
    if month in [6, 7, 8]:
        return "Summer"
    elif month in [10, 11, 12]:
        return "Winter"
    else:
        return None

def seasonal_yearly_means(df):
    df = df.copy()
    df["century"] = df["year"].apply(assign_century)
    df["season"] = df["month"].apply(assign_season)

    df = df.dropna(subset=["century", "season"])

    yearly = (
        df.groupby(["year", "century", "season"])
          ["t_corr"]
          .mean()
          .reset_index()
    )
    return yearly