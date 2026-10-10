#Demonstrate Factor data structure in R.
# create a vector of categorical data
data <- c("A", "B", "A", "C", "B", "A")

# create a factor object
factor_data <- factor(data)

# view the levels of the factor
levels(factor_data)

# view the frequency of each level
table(factor_data)
