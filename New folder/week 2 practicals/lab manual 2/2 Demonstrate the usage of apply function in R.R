# Create a matrix
matrix_data <- matrix(1:9, nrow = 3)

# Define a custom function to calculate the square root of each element
sqrt_element <- function(x) {
  sqrt(x)
}

# Apply the function to each column of the matrix
result <- apply(matrix_data, 2, sqrt_element)

# Print the result
print(result)
