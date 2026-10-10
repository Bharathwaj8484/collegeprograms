#Write a R program to create a list of 
#elements using vectors, matrices and a functions. Print the content of the list.  

my_vector <- c(1, 2, 3, 4, 5)
my_matrix <- matrix(1:9, nrow = 3, ncol = 3)
my_function <- function(x) {
  x^2
}

my_list <- list(my_vector, my_matrix, my_function)

print(my_list)
