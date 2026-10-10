# Calculate mean, minimum, maximum, and sum values
mean_tree <- colMeans(trees)
min_tree <- sapply(trees, min)
max_tree <- sapply(trees, max)
sum_tree <- colSums(trees)

# Create data frame 'A'
A <- data.frame(
  Girth = c(mean_tree["Girth"], min_tree["Girth"], max_tree["Girth"], sum_tree["Girth"]),
  Height = c(mean_tree["Height"], min_tree["Height"], max_tree["Height"], sum_tree["Height"]),
  Volume = c(mean_tree["Volume"], min_tree["Volume"], max_tree["Volume"], sum_tree["Volume"]),
  row.names = c("mean_tree", "min_tree", "max_tree", "sum_tree")
)

# Print data frame 'A'
print(A)
