# Create the first buildings data frame
buildings <- data.frame(
  location = c(1, 2, 3),
  name = c("building1", "building2", "building3")
)

# Create the second buildings data frame
buildings2 <- data.frame(
  location = c(5, 4, 6),
  name = c("building5", "building4", "building6")
)

# Merge the rows of the two data frames vertically
allBuildings <- rbind(buildings, buildings2)

# Print the merged data frame allBuildings
print(allBuildings)
