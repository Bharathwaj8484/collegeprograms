# declaring and creating a list
lst <- list(ele1 = 1:5,       
            ele2 = c(FALSE,TRUE),
            ele3 = LETTERS[4:9])

# printing list contents
print ("List contents : ")
print (lst)

# accessing elements
print ("Accessing elements : ")
print(lapply(seq_along(lst),
             function(i) paste(names(lst)[[i]],
                               "->",
                               paste(lst[[i]],collapse = ","))))
