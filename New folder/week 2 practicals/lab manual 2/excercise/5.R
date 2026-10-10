# Remove variables Sex and Code from N
N_updated <- subset(N, select = -c(Sex, Code))

# Create the new data frame with values and ind columns
new_df <- stack(N_updated)

# Rename the columns
colnames(new_df) <- c("values", "ind")

# Print the new data frame
print(new_df)
