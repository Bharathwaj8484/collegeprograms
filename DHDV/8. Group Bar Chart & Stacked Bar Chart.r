library(RColorBrewer)
months <- c("Jan", "Feb", "Mar", "Apr", "May")
regions <- c("West", "North", "South")
values <- matrix(c(21, 32, 33, 14, 95, 46, 67, 78, 39, 11, 22,
                   23, 94, 15, 16), nrow = 3, ncol = 5, byrow = TRUE)
barplot(values, main = "Total Revenue", names.arg = months, xlab = "Month",
        ylab = "Revenue", col = c("cadetblue3", "deeppink2", "goldenrod1"))
legend("topleft", regions, cex = 1.3,
       fill = c("cadetblue3", "deeppink2", "goldenrod1"))
