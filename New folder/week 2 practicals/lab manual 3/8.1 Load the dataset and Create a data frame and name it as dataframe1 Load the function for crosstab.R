# Create the dataframe1
dataframe1 <- data.frame(
  Reference = c("KRXH", "KRPT", "FHRA", "CZKK", "CQTN", "PZXW", "SZRZ", "RMZE", "STNX", "TMDW"),
  Status = c("Accepted", "Accepted", "Rejected", "Accepted", "Rejected", "Accepted", "Rejected", "Rejected", "Accepted", "Accepted"),
  Gender = c("Female", "Male", "Male", "Female", "Female", "Female", "Male", "Female", "Female", "Female"),
  TestNewOrFollowUp = c("Test1", "Test1", "Test2", "Test3", "Test1", "Test4", "Test4", "Test2", "Test3", "Test1")
)

# Load the function for crosstab
crosstab <- function(x, y) table(factor(x), factor(y))
# Perform cross-tabulation analysis
cross_tab <- crosstab(dataframe1$Status, dataframe1$Gender)
cross_tab

#OR METHOD

library(stats)
status_gender_table <- xtabs(~ Status + Gender, data = dataframe1)
print(status_gender_table)

table <- xtabs(~Reference+Status, data=dataframe1)
print(table)

