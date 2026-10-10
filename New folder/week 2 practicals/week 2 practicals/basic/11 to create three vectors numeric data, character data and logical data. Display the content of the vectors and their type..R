#Write a R program to create three vectors numeric data, character data and logical data. 
#Display the content of the vectors and their type.  
# Create a vector of numeric data
num_vec <- c(1.2, 3.4, 5.6, 7.8, 9.0)

# Create a vector of character data
char_vec <- c("apple", "banana", "cherry", "date", "elderberry")

# Create a vector of logical data
log_vec <- c(TRUE, FALSE, TRUE, FALSE, TRUE)

# Display the content of the vectors
print(num_vec)
print(char_vec)
print(log_vec)

# Display the data type of the vectors
cat("num_vec is of type:", class(num_vec), "\n")
cat("char_vec is of type:", class(char_vec), "\n")
cat("log_vec is of type:", class(log_vec), "\n")
