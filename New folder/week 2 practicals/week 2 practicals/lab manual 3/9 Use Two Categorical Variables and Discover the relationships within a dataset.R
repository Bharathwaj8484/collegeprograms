# i) Discover relationships within a dataset using two categorical variables
relationships <- table(dataframe1$Reference, dataframe1$Status)
relationships

# ii) Create a table delineating the relationship between "Reference" and "Status" using xtabs()
relationship_table <- xtabs(~ Reference + Status, data = dataframe1)
relationship_table

# iii) Save the table as dataframe2
dataframe2 <- relationship_table
