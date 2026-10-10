names<-c("joseph","samueal","ricky","frank","matt murdock","geroge","walter","butcher","Tommy vercetti","kage","rdj","sus","sr","oliver queen","patrick")
age<-c(32,37,27,21,42,54,64,44,32,21,17,65,34,33,54)
bmi<-c(18,17.4,16.5,18.2,19,19.3,21.2,21.5,22.1,20.7,23.1,17.9,30.2,17.3,16.9)
id<-c(201,745,874,272,857,453,563,434,785,823,567,546,567,567,127)
bmidf<-data.frame(names,bmi,age,id) 
View(bmidf)
write.csv(bmidf,"bmidf.csv")  

