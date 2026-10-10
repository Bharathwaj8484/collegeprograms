#Deconstruct a matrix in R 
A <- matrix(c(1, 2, 3, 4), nrow = 2)

# extract rows and columns as vectors
row1 <- A[1, ]
row2 <- A[2, ]
col1 <- A[, 1]
col2 <- A[, 2]

# print the vectors
print(row1)
print(row2)
print(col1)
print(col2)

