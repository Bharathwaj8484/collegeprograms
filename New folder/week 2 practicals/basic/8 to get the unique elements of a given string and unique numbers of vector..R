# Create a string and a vector with duplicate elements
my_string <- "hello world"
my_vector <- c(1, 2, 3, 2, 4, 1)

# Get the unique elements of the string
unique_string <- unique(strsplit(my_string, "")[[1]])

# Get the unique numbers of the vector
unique_vector <- unique(my_vector)

# Print the results
cat("Unique elements of the string:", unique_string, "\n")
cat("Unique numbers of the vector:", unique_vector, "\n")
