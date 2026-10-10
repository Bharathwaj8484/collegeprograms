data<-read.csv("travel-times.csv")
View(data)
hist(data$Distance,col="red",xlab = "Height Bin",main = "Histogram of Tree heights")