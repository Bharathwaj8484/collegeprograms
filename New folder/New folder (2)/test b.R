df<-read.csv("mtcars.csv")
# Load the mtcars dataset
data(mtcars)

# Create a logistic regression model using hp, wt, and cyl as predictors and am as the response variable
model <- glm(am ~ hp + wt + cyl, data = mtcars, family = binomial)

# Print a summary of the model
print(summary(model))
