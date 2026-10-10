# Install the "tigerstats" package if not already installed
# install.packages("tigerstats")

# Load the "tigerstats" package
library(tigerstats)

# Cross-tabulate "Status" and "Test"
cross_tab <- xtabs(~ Status + TestNewOrFollowUp, data = dataframe1)

# Display column percentages for "Status" by "Test"
col_perc <- colPerc(cross_tab)
col_perc
