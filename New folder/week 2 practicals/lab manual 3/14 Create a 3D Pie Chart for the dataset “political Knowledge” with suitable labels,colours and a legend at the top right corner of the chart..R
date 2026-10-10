# Install and load the required package
# install.packages("plotrix")
library(plotrix)

# Dataset "political Knowledge"
political_knowledge <- c(12, 25, 15, 8)
labels <- c("Low", "Medium", "High", "Very High")
colors <- c("#FFC300", "#FF5733", "#C70039", "#900C3F")

# Create the 3D pie chart
pie3D(political_knowledge, labels = labels, explode = 0.1, col = colors)

# Add a legend at the top right corner
legend("topright", legend = labels, fill = colors)

# Add a title to the chart
title(main = "Political Knowledge 3D Pie Chart")
