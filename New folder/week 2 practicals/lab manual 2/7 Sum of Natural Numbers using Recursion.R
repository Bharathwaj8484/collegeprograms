# Recursive function to calculate the sum of natural numbers
sum_natural <- function(n) {
  if (n <= 1) {
    return(n)  # Base case: return 1 for n = 1, 0 for n = 0
  } else {
    return(n + sum_natural(n - 1))  # Recursive call
  }
}

# Calculate the sum of natural numbers up to a given value
n <- 10
result <- sum_natural(n)

# Print the result
print(result)
