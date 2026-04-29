"""Does the analysis."""
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("../../data/uppsala_tm_1722-2022.dat",sep=r"\s+")
print(df) # noqa: T201 # We really need that print statement
df.columns=["Year","Month","Day","T","Tcorr","Data id"]
print(df.Tcorr) # noqa: T201 # We really need that print statement
df["Date"]=pd.to_datetime(df[["Year", "Month", "Day"]])

ax = df.plot(x="Date",y="Tcorr")
ax.set(xlabel="Year", ylabel="T", title="Time series Corrected temperature")
fig = ax.get_figure()
fig.savefig("T_Uppsala.png")

plt.show()


