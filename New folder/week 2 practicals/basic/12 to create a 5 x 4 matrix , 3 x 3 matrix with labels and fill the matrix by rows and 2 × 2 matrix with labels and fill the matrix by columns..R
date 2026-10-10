#Write a R program to create a 5 x 4 matrix , 3 x 3 matrix with labels and fill the matrix by 
#rows and 2 × 2 matrix with labels and fill the matrix by columns.  
# Create a 5 x 4 matrix filled by rows
matrix1 <- matrix(1:20, nrow=5, ncol=4, byrow=TRUE)

# Create a 3 x 3 matrix with labels and fill by rows
matrix2 <- matrix(c(1,2,3,4,5,6,7,8,9), nrow=3, ncol=3,
                  dimnames=list(c("row1", "row2", "row3"),
                                c("col1", "col2", "col3")))

# Create a 2 x 2 matrix with labels and fill by columns
matrix3 <- matrix(c(1,2,3,4), nrow=2, ncol=2,
                  dimnames=list(c("row1", "row2"),
                                c("col1", "col2")), byrow=FALSE)

# Print the matrices
print(matrix1)
print(matrix2)
print(matrix3)
