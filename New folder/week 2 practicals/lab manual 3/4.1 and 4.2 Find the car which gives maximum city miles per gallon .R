mpg<-read.csv("C:\\Users\\bhara\\OneDrive\\Documents\\mpg.csv")
mpg


# i) Find the car which gives maximum city miles per gallon
max_city_mpg <- mpg[which.max(mpg$cty), "model"]
max_city_mpg

# ii) Find the cars which gives minimum disp in compact and subcompact class
compact_cars <- mpg[mpg$class %in% c("compact", "subcompact"), ]
min_disp_compact <- compact_cars[which.min(compact_cars$displ), "model"]
min_disp_compact