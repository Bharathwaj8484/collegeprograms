# Create a list
my_list <- list(a = 1:3, b = 4:6, c = 7:9)

# Define a custom function to calculate the square of a value
square <- function(x) {
  x^2
}

# Apply the function to each element of the list using sapply
result <- sapply(my_list, square)

# Print the result
print(result)
