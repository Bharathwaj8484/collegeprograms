# Create a vector
values <- c(1, 2, 3, 4, 5, 6)

# Create a factor indicating groups
groups <- factor(c("A", "A", "B", "B", "B", "A"))

# Apply the sum function to subsets based on groups
result <- tapply(values, groups, sum)

# Print the result
print(result)
