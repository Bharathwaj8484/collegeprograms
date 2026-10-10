thismatrix <- matrix(c("apple","banana","cherry","orange","grape","pineapple","pear","melon","fig"), nrow =3, ncol =3)
newmatrix <-cbind(thismatrix, c("strawberry","blueberry","raspberry"))
print(t(newmatrix))
print(length(thismatrix))
