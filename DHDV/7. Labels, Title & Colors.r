h <- c(12, 35, 54, 3, 41)
m <- c("Feb", "Mar", "Apr", "May", "Jun")
barplot(h, names.arg = m, xlab = "Month", ylab = "Revenue", col = "Green",
        main = "Revenue Bar chart", border = "red")
