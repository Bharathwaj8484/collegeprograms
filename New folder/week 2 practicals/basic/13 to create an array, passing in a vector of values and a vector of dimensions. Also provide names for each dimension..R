#Write a R program to create an array, passing in a vector of values and a vector 
#of dimensions. Also provide names for each dimension.  

values <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
dims <- c(3, 2, 2)
my_array <- array(values, dims, dimnames = list(c("Row 1", "Row 2", "Row 3"), c("Col 1", "Col 2"), c("Depth 1", "Depth 2")))
print(my_array)
