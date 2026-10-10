library(tigerstats)
# Cross-tabulate "Status" and "Test"
cross_tab <- xtabs(~ Status + TestNewOrFollowUp, data = dataframe1)
cross_tab
# Display row percentages for "Status" by "Test"
row_perc <- rowPerc(cross_tab)
row_perc

