set.seed(20) 
clusters<-kmeans(diabetesX[,2:3], 5)
diabetesX$Borough<- as.factor(clusters$cluster)
str(clusters)
