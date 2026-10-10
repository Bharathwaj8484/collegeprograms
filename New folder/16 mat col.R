# Create a matrix
mat <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9), nrow = 3)

# Access the element at 3rd column and 2nd row
element <- mat[2, 3]
print(element)

# Access only the 3rd row
row <- mat[3, ]
print(row)

# Access only the 4th column
col <- mat[, 4]
print(col)
