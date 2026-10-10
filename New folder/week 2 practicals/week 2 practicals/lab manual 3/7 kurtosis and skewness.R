library(e1071)
library(ggplot2)

# a) Find the skewness of city miles per mileage in the "mpg" dataset
skewness_city_mpg <- skewness(mpg$cty)
skewness_city_mpg

# b) Find the kurtosis of city miles per mileage in the "mpg" dataset
kurtosis_city_mpg <- kurtosis(mpg$cty)
kurtosis_city_mpg

# Create a qplot for the city miles per mileage column
qplot(mpg$cty, geom = "histogram", bins = 20, xlab = "City Miles Per Gallon")
