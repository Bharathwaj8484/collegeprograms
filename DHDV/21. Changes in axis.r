library(ggplot2)
plot_object <- ggplot(mtcars, aes(x = log(mpg), y = log(drat))) +
  geom_point(aes(color = factor(gear)))
print(plot_object)
