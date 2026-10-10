#Write a R program to create a vector which 
#contains 10 random integer values between -50 and +50.  

# Create a vector with 10 random integer values between -50 and +50
x <- sample(-50:50,10)
cat("Random integer values between -50 and +50:", x)
