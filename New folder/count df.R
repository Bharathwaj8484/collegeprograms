# loading the reqd library
library ("stringr")

# creating a data frame
data_frame <- data.frame(
  col1 = c(1:5), col2 = c("Geeks","for","geeks","CSE","portal"))

# character to search for
ch <- "e|E"

# counting the occurrences of character
count <- str_count(data_frame$col2, ch)
print ("Count of e :")
print (count)
print(sum(count))