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

  # I think this is better for visualization
  data %>% group_by(Year) %>% summarise(mean_T = mean(Temperature_Corrected))
    
  p <- ggplot(data %>% group_by(Year) %>% summarise(mean_T = mean(Temperature_Corrected)), 
              aes(Year, mean_T)) + geom_point() + geom_smooth(method='lm', formula= y~x)
  ggsave("~/programming_formalisms_project_summer_2026/programming_formalisms_project_summer_2026/learners/JGC/plot.png", p, device = "png")
}

do_experiment()

files <- list.files("~/programming_formalisms_project_summer_2026/programming_formalisms_project_summer_2026/learners/JGC/")  
"regression.txt" %in% files == TRUE
"plot.png" %in% files == T
