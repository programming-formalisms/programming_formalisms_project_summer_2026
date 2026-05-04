**Research question:** Is there any difference in the temperatures measured in Uppsala in the period 1722-2022?


**Null Hypothesis:** There is no difference.


**Method:** We consider only complete years to take into account seasonal changes. 
We divide the data in three groups and calculate the average, standard deviation and confidence interval.
We calculate the p-value for the difference between all three groups. The results are significant when p<0.05. The package produces a box plot figure and text file stating the significance.

**Requirements:**
R1: is able to open a temperatures file.
R2: if chosen, incomplete year data is discarded.
R3: if chosen, incomplete year data is filled in with bootstrapping using surrounding years.
R4: split data into three groups.
R5: average, standard deviation and confidence interval are calculated for each group.
R6: run Kolgomorov-Smirnoff test on data.
R7: a plot containing boxplots and violin plots per group is produced.

Victoria and Claudia
