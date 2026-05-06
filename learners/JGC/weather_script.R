library(tidyverse)
library(ggplot2)

do_experiment <- function() {
  columns <- c("Year", "month", "day", "Temperature", "Temperature_Corrected", "Place")
  data <- read.table("~/programming_formalisms_project_summer_2026/data/uppsala_tm_1722-2022.dat", col.names = columns)
  
  fit_Data <- lm(data[,5] ~ data[,1])
  summ_data <- summary(fit_Data)
  print(summ_data)
  
  sink("~/programming_formalisms_project_summer_2026/programming_formalisms_project_summer_2026/learners/JGC/regression.txt")
  print(summ_data)
  sink()
  
  p <- ggplot(data, aes(Year, Temperature_Corrected)) + geom_point() + geom_smooth(method='lm', formula= y~x)
  ggsave("~/programming_formalisms_project_summer_2026/programming_formalisms_project_summer_2026/learners/JGC/plot.png", p, device = "png")
}

files <- list.files("~/programming_formalisms_project_summer_2026/programming_formalisms_project_summer_2026/learners/JGC/")  
"regression.txt" %in% files == TRUE
