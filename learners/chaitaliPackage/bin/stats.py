import numpy as np
from scipy.stats import ttest_ind, mannwhitneyu

def compare_to_reference(yearly_df, reference="1722–1821", season="Summer"):
    ref = yearly_df[
        (yearly_df["century"] == reference) &
        (yearly_df["season"] == season)
    ]["t_corr"]

    results = {}

    for century in yearly_df["century"].unique():
        if century == reference:
            continue

        cur = yearly_df[
            (yearly_df["century"] == century) &
            (yearly_df["season"] == season)
        ]["t_corr"]

        t_p = ttest_ind(ref, cur, equal_var=False).pvalue
        u_p = mannwhitneyu(ref, cur, alternative="two-sided").pvalue

        d = (cur.mean() - ref.mean()) / np.sqrt(
            (cur.var() + ref.var()) / 2
        )

        results[century] = {
            "delta_T": cur.mean() - ref.mean(),
            "p_ttest": t_p,
            "p_mannwhitney": u_p,
            "cohens_d": d
        }

    return results