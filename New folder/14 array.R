# Create the data
col1 <- c(1, 2, 3)
col2 <- c(4, 5, 6)
col3 <- c(7, 8, 9)
col4 <- c(10, 11, 12)
table1 <- data.frame(col1, col2)
table2 <- data.frame(col3, col4)

# Create the array
my_array <- array(c(table1$col1, table1$col2, table2$col3, table2$col4),
                  dim = c(3, 4, 2),
                  dimnames = list(c("row1", "row2", "row3"),
                                  c("col1", "col2", "col3", "col4"),
                                  c("table1", "table2")))

# Display the content of the array
print(my_array)
