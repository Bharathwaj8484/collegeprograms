# Load the "datasets" package (if not already loaded)
library(datasets)

# Access the "mtcars" dataset
data(mtcars)

# Create the boxplot graph
boxplot(mpg ~ cyl, data = mtcars, xlab = "Number of Cylinders", ylab = "Miles per Gallon", 
        main = "Boxplot of MPG by Cylinder Count")
