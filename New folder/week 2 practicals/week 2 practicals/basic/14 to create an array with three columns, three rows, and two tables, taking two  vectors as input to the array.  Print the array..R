#Write a R program to create an array with three columns, three rows, and two "tables",
#taking two  vectors as input to the array.  Print the array.  

vec1 <- c(1, 2, 3, 4, 5, 6, 7, 8, 9)
vec2 <- c(10, 11, 12, 13, 14, 15, 16, 17, 18)

my_array <- array(c(vec1, vec2), dim = c(3, 3, 2))


print(my_array)

