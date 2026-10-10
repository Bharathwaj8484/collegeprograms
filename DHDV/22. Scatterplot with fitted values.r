library(ggplot2)
plot_object <- ggplot(mtcars, aes(x = log(mpg), y = log(drat))) +
  geom_point(aes(color = factor(gear))) +
  stat_smooth(method = "lm", col =  "#C42126", se = FALSE, size = 1)
print(plot_object)
