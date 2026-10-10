#Write a R program to take input from the user (name and age) and display the values. 
#Also print the version of R installation.  

name <- readline(prompt = "Enter your name: ")
age <- readline(prompt = "Enter your age: ")


cat("Your name is:", name, "\n")
cat("Your age is:", age, "\n")

cat("R version:", R.version.string, "\n")