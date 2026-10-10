#Demonstrate the creation of S4 class in R.
# define a new S4 class
setClass("Person",
         representation(name = "character",
                        age = "numeric",
                        gender = "character"))

# create an instance of the Person class
person1 <- new("Person", name = "John", age = 25, gender = "M")

# define a show method for the Person class
setMethod("show", "Person",
          function(object) {
            cat("Name: ", object@name, "\n")
            cat("Age: ", object@age, "\n")
            cat("Gender: ", object@gender, "\n")
          })

# print the person1 object
person1
