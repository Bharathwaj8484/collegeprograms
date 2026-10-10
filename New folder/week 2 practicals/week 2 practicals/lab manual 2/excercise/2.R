# Create the second data frame
df2 <- df[df$Letter %in% c("a", "y"), c("Id", "x", "y")]
df2 <- reshape(df2, idvar = "Id", timevar = "Letter", direction = "wide")
df2 <- df2[, c("Id", "x.a", "y.a", "x.y", "y.y")]
df2 <- df2[order(df2$Id), ]

# Print the second data frame
print(df2)