# Create two vectors
vector1 <- c(1, 2, 3)
vector2 <- c(4, 5, 6)

# Define a custom function to calculate the sum of two values
sum_elements <- function(x, y) {
  x + y
}

# Apply the function to corresponding elements of the vectors using mapply
result <- mapply(sum_elements, vector1, vector2)

# Print the result
print(result)
