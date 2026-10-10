#Demonstrate the creation of Reference class in R by defining a class called students with 
#fields – Name, Age , GPA. Also illustrate how the fields of the object can be accessed using the $ operator. 
#Modify the Name field by reassigning the name to Paul.

# Define the Reference Class
setRefClass("students",
            fields = list(
              Name = "character",
              Age = "numeric",
              GPA = "numeric"
            )
)

# Create an instance of the students class
student1 <- students(Name="John", Age=25, GPA=3.8)

# Accessing fields using the $ operator
print(student1$Name)
print(student1$Age)
print(student1$GPA)

# Modify the Name field
student1$Name <- "Paul"
print(student1$Name)
