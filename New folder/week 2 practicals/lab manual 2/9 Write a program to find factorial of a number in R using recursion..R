# Recursive function to find factorial
factorial <- function(n) {
  if (n <= 1) {
    return(1)  # Base case: factorial of 0 and 1 is 1
  } else {
    return(n * factorial(n - 1))  # Recursive call
  }
}

# Find factorial of a given number
num <- 5  # Number to find factorial
result <- factorial(num)

# Print the factorial
print(result)
