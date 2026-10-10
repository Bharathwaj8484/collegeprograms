# Load the "datasets" package (if not already loaded)
library(datasets)

# Access the "AirPassengers" dataset
data(AirPassengers)

# Set the bin width and starting point on the x-axis
bin_width <- 200
x_start <- 100

# Create the histogram
hist(AirPassengers, breaks = seq(x_start, max(AirPassengers) + bin_width, bin_width),
     xlab = "Passenger Count", ylab = "Frequency", main = "Histogram of AirPassengers")
