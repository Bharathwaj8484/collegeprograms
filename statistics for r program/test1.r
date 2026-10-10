# Load the USArrests dataset
data(USArrests)

# (i) a. Explore the summary of Data set
summary(USArrests)

# Print the structure of the dataset
str(USArrests)

# (i) b. Print the state which saw the largest total number of rape
USArrests[which.max(USArrests$Rape), "State"]

# (i) c. Print the states with the max & min crime rates for murder
USArrests[which.max(USArrests$Murder), "State"]
USArrests[which.min(USArrests$Murder), "State"]