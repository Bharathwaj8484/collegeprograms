#Perform array manipulation in R .

# create a 3-dimensional array
arr <- array(data = 1:24, dim = c(2, 3, 4))
print(arr)


#Indexing arrays
# access an element of the array
elem <- arr[1, 2, 3]
print(elem)


#Reshape an array:
# reshape the array
new_arr <- array(data = 1:24, dim = c(4, 3, 2))
dim(arr) <- c(2, 6)
print(arr)


#Transpose an array:
# transpose the array
trans_arr <- aperm(arr, c(2, 1, 3))
print(trans_arr)


