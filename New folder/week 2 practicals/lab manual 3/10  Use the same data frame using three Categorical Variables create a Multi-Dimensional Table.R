# Create a multi-dimensional cross-tabulation of "Status", "Gender", and "Test"
multi_dimensional_table <- table(dataframe1$Status, dataframe1$Gender, dataframe1$TestNewOrFollowUp)
multi_dimensional_table
