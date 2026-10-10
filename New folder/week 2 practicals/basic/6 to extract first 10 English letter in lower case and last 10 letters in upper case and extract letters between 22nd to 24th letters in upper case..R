# Create a character vector containing the English alphabet
alphabet <- letters

# Extract the first 10 letters in lowercase
first<- alphabet[1:10]

# Extract the last 10 letters in uppercase
last<- toupper(alphabet[17:26])

# Extract letters between 22nd and 24th in uppercase
middle<- toupper(alphabet[22:24])

# Print the results
cat("First 10 letters in lowercase:", first, "\n")
cat("Last 10 letters in uppercase:", last, "\n")
cat("Letters between 22nd and 24th in uppercase:", middle, "\n")
