# Create data frame XY
X <- c(1, 2, 3, 1, 4, 5, 2)
Y <- c(0, 3, 2, 0, 5, 9, 3)
XY <- data.frame(X, Y)

# Look at duplicated elements in XY
duplicates <- duplicated(XY)
print(XY[duplicates, ])

# Keep only the unique lines in XY
unique_lines <- unique(XY)
print(unique_lines)
