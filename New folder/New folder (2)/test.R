df<-read.csv("USArrests.csv")
print(summary(USArrests))
print("****************************")
print(dim(USArrests))

cat("\n")
# Mean of each variable 
cat("mean",mean(USArrests$Murder),
mean(USArrests$Assault),
mean(USArrests$UrbanPop),
mean(USArrests$Rape),"\n")

cat("\n")
# Median of each variable
cat("median",median(USArrests$Murder),
median(USArrests$Assault),
median(USArrests$UrbanPop),
median(USArrests$Rape),"\n")

cat("\n")
# Range of each variable
cat("range",range(USArrests$Murder),
range(USArrests$Assault),
range(USArrests$UrbanPop),
range(USArrests$Rape),"\n")

cat("\n")
# Standard deviation of each variable
cat("sd",sd(USArrests$Murder),
sd(USArrests$Assault),
sd(USArrests$UrbanPop),
sd(USArrests$Rape),"\n")

cat("\n")
# Variance of each variable
cat("var",var(USArrests$Murder),
var(USArrests$Assault),
var(USArrests$UrbanPop),
var(USArrests$Rape),"\n")
cat("\n")
cat("cor",cor(USArrests))

cat("\n  i b")
#b
# Find the index of the state with the largest total number of rape
max<-which.max(USArrests$Rape)

# Extract the name of the state with the largest total number of rape
state<- row.names(USArrests)[max]

# Print the state name
cat("\nThe state with the largest total number of rape is", state)

cat("\n i c")
#c
# Find the indices of the states with the highest and lowest murder rates
max1<- which.max(USArrests$Murder)
min<- which.min(USArrests$Murder)

# Extract the names of the states with the highest and lowest murder rates
state2<- row.names(USArrests)[max1]
state3<- row.names(USArrests)[min]

# Print the state names
cat("\nThe state with the highest murder rate is", state2, "\n")
cat("\nThe state with the lowest murder rate is", state3, "\n")

library(plotrix)
cat("ii(a)")
# Calculate the correlation matrix for the features
cor<- cor(USArrests)

# Print the correlation matrix
print(cor)

cat("\n b")
# Calculate the median assault arrest rate for all states
median<- median(USArrests$Assault)

high<- USArrests[USArrests$Assault > median, ]

# Print the names of the states with high assault arrest rates
cat("\nThe following states have an assault arrest rate greater than the median:", "\n")
cat(row.names(high), "\n")

cat("\n c")
# Calculate the 25th percentile of the murder rate for all states
murder<- quantile(USArrests$Murder, 0.25)

# Subset the data set to include only the rows with a murder rate less than or equal to the 25th percentile
low<- USArrests[USArrests$Murder <= murder, ]

# Print the names of the states with low murder rates
cat("\nThe following states are in the bottom 25% of murder rates:", "\n")
cat(row.names(low), "\n")

cat("\n iii")
# Create a histogram of murder arrests by state
hist(USArrests$Murder)

# Create a density plot of murder arrests by state
plot(density(USArrests$Murder))

cat("\n iii b")
# Create a scatter plot of murder arrest rate vs. urban population proportion
plot(x = USArrests$UrbanPop, y = USArrests$Murder, 
     main = "Murder Arrests vs. Urban Population Proportion", 
     xlab = "Urban Population Proportion", ylab = "Murder Arrests", 
     pch = 19)

# Add points to the scatter plot colored by assault arrest rates
points(x = USArrests$UrbanPop, y = USArrests$Murder, 
       col = USArrests$Assault, pch = 19)

# Add a color scale legend to the plot
legend("topright", legend = "Assault Arrests", 
       fill = rev(colorRampPalette(c("blue", "red"))(10)), 
       bty = "n", ncol = 1, cex = 0.8)

cat("\n iii c ")
# Create a vector of murder rates for each state
murder_rates <- USArrests$Murder

# Create a barplot of murder rates for each state
barplot(murder_rates, names.arg = rownames(USArrests), 
        main = "Murder Rates by State", xlab = "State", ylab = "Murder Rate", 
        col = "steelblue", las = 2, cex.names = 0.6)



