my_factor <- factor(c("C", "A", "B", "B", "C", "A"))
# Define the new order of levels
new_levels <- c("A", "B", "C")

# Use the factor() function to reorder the levels
print(my_factor <- factor(my_factor, levels = new_levels))
