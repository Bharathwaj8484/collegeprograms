#) Perform the operation of combining matrices in R using cbind() and rbind() functions.

A <- matrix(c(1, 2, 3, 4), nrow = 2)
B <- matrix(c(5, 6, 7, 8), nrow = 2)

# combine matrices horizontally using cbind()
C <- cbind(A, B)
print(C)

# combine matrices vertically using rbind()
D <- rbind(A, B)
print(D)
