# Recursive function to generate Fibonacci sequence
fibonacci <- function(n) {
  if (n <= 1) {
    return(n)  # Base case: return n for n = 0 and 1
  } else {
    return(fibonacci(n - 1) + fibonacci(n - 2))  # Recursive call
  }
}

# Generate Fibonacci sequence up to a given number of terms
num_terms <- 10  # Number of terms to generate
sequence <- sapply(0:(num_terms-1), fibonacci)

# Print the Fibonacci sequence
print(sequence)
