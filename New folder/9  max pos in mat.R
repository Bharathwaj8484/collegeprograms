# Create a matrix
mat <- matrix(c(1, 2, 3, 4, 9, 6,4,5), nrow = 2,ncol = 4)
print(mat)

# Get the position of the maximum element in each row
max_positions <- max.col(mat)

# Print the result
print(max_positions)
