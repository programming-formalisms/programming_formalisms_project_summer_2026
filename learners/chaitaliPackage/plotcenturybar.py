from chaitali.io import read_uppsala_dat
from chaitali.aggregate import seasonal_yearly_means
from chaitali.plot import plot_century_bars
from chaitali.stats import compare_to_reference

df = read_uppsala_dat("uppsala_tm_1722-2022.dat")
yearly = seasonal_yearly_means(df)

plot_century_bars(yearly)

summer_stats = compare_to_reference(yearly, season="Summer")
winter_stats = compare_to_reference(yearly, season="Winter")

print("Summer:", summer_stats)
print("Winter:", winter_stats)