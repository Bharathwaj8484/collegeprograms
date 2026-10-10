library(ggplot2)
plot_object <- ggplot(mtcars, aes(x = drat, y = mpg)) + geom_point()
print(plot_object)
