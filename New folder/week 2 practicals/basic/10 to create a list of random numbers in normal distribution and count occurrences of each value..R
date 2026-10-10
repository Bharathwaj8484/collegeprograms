#Write a R program to create a list of random numbers in normal distribution 
#and count occurrences of each value.  
# Set the seed for reproducibility
set.seed(123)

# Create a list of 1000 random numbers in normal distribution
my_list <- rnorm(1000)

# Count the occurrences of each value in the list
my_count <- table(my_list)

# Print the count
print(my_count)

