import pandas as pd
import matplotlib.pyplot as plt
import datetime

df=pd.read_csv("../../data/uppsala_tm_1722-2022.dat",sep='\s+')
print(df)
df.columns=['Year','Month','Day','T','Tcorr','Data id']
print(df.Tcorr)
df['Date']=pd.to_datetime(df[["Year", "Month", "Day"]])

ax = df.plot(x='Date',y='Tcorr')
ax.set(xlabel='Year', ylabel='T', title='Time series Corrected temperature')
fig = ax.get_figure()
fig.savefig('T_Uppsala.png')

plt.show()


