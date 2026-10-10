# Input vectors
H <- c(7, 12, 28, 3, 41)
M <- c("mar", "apr", "may", "jun", "jul")

# Create the box plot
boxplot(H, main = "Revenue chart", xlab = "Month", ylab = "Revenue",col=c("red"))

# Add labels to the x-axis
axis(1, at = 1:length(M), labels = M)

# Add a legend
legend("topright", legend = "H", fill = "red")

# Add a title to the chart
title(main = "Revenue chart")
