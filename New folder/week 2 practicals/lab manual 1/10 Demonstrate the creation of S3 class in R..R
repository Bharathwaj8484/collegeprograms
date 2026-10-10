#Demonstrate the creation of S3 class in R.


setClass("Person",
         slots = list(name = "character",
                      age = "numeric",
                      gender = "character"))

# create an instance of the Person class
person1 <- list(name = "John", age = 25, gender = "M")
class(person1) <- "Person"

# define a print method for the Person class
print.Person <- function(x) {
  cat("Name: ", x@name, "\n")
  cat("Age: ", x@age, "\n")
  cat("Gender: ", x@gender, "\n")
}

# print the person1 object
print(person1)
