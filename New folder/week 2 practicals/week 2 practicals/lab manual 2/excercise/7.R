# Order the data frame by the first column
A <- A[order(A[, 1]), ]

# Rename the row names
row.names(A) <- c("mean", "min", "max", "tree")

# Print the updated data frame 'A'
print(A)
