# Install and load the required package
# install.packages("plotrix")
library(plotrix)

# Input vector and corresponding labels
values <- c(21, 62, 10, 53)
labels <- c("London", "New York", "Singapore", "Mumbai")

# Create the pie chart
pie(values, labels = labels, main = "City Pie-Chart")

# Add a legend at the top right corner
legend("topright", legend = labels, fill = rainbow(length(labels)))

# Add a title to the chart
title(main = "City Pie-Chart")
