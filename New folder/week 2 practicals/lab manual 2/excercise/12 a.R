# Create the buildings data frame
buildings <- data.frame(
  location = c(1, 2, 3),
  name = c("building1", "building2", "building3")
)

# Create the data data frame
data <- data.frame(
  survey = c(1, 1, 1, 2, 2, 2),
  LocationID = c(1, 2, 3, 2, 3, 1),
  efficiency = c(51, 64, 70, 71, 80, 58)
)

# Merge the buildings and data data frames
buildingStats <- merge(buildings, data)

# Print the merged data frame buildingStats
print(buildingStats)

