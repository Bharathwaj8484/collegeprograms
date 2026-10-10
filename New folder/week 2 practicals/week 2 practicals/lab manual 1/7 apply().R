#Perform calculations across array elements in an array using the apply () function.
# create a matrix
mat <- matrix(c(1, 2, 3, 4, 5, 6), nrow = 2)

# calculate the mean of each row using apply()
row_means <- apply(mat, MARGIN = 1, FUN = mean)

# print the row means
print(row_means)


#You can also use the apply() function to perform calculations across columns of an array by specifying MARGIN = 2. Here is an example of how to calculate the sum of each column of a matrix

# create a matrix
mat <- matrix(c(1, 2, 3, 4, 5, 6), nrow = 2)

# calculate the sum of each column using apply()
col_sums <- apply(mat, MARGIN = 2, FUN = sum)

# print the column sums
print(col_sums)
