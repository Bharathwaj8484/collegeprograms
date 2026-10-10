# Create the buildings3 data frame with additional variables
buildings3 <- data.frame(
  location = c(7, 8, 9),
  name = c("building7", "building8", "building9"),
  startEfficiency = c(75, 87, 91)
)

# Create a new buildings3 data frame without the extra variables
buildings3 <- buildings3[, c("location", "name")]

# Print the updated buildings3 data frame
print(buildings3)

