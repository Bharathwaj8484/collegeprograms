# Create df3
df3 <- data.frame(Id = c(4, 3, 2, 1), score = c(100, 98, 94, 99))

# Merge M and df3 to create N
N <- merge(M, df3, by = "Id")

# Print the data frame N
print(N)
