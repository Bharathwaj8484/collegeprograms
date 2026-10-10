# Create df1 and df2
df1 <- data.frame(Id = 1:4, Age = c(14, 12, 15, 10))
df2 <- data.frame(Id = 1:4, Sex = c("F", "M", "M", "F"), Code = c("a", "b", "c", "d"))

# Merge df1 and df2 to create M
M <- merge(df1, df2, by = "Id")

# Print the data frame M
print(M)
