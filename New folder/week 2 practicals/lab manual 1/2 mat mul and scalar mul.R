#Perform Scalar multiplication and matrix multiplication in R

A <- matrix(c(1, 2, 3, 4), nrow = 2)

# scalar multiplication
B <- 2 * A
print(B)

# matrix multiplication
C <- A %*% B
print(C)
