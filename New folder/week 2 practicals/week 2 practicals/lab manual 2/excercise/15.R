# Create the buildings3 data frame with an additional variable
buildings3 <- data.frame(
  location = c(7, 8, 9),
  name = c("building7", "building8", "building9"),
  startEfficiency = c(75, 87, 91)
)

# Append the new variable from buildings3 to buildings and buildings2
buildings <- cbind(buildings, buildings3$startEfficiency)
buildings2 <- cbind(buildings2, buildings3$startEfficiency)

# Set the corresponding values in buildings and buildings2 to NA
buildings[, "startEfficiency"] <- NA
buildings2[, "startEfficiency"] <- NA

# Print the updated buildings and buildings2 data frames
print(buildings)
print(buildings2)
