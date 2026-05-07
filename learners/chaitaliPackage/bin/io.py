import pandas as pd

def read_uppsala_dat(path):
    df = pd.read_csv(
        path,
        delim_whitespace=True,
        header=None,
        names=["year", "month", "day", "t_raw", "t_corr", "source_id"],
        na_values=["."]
    )
    return df