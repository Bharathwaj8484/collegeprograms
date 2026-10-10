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

# Create a cross join by generating all combinations of rows
buildingStats <- expand.grid(buildings, data)

# Print the column names of the merged data frame buildingStats
colnames(buildingStats)
