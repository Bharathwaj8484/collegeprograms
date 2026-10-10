library(ggplot2)
new_graph <- ggplot(mtcars, aes(x = log(mpg), y = log(drat))) +
  geom_point(aes(color = factor(gear))) +
  stat_smooth(method = "lm", col = "#C42126", se = FALSE, size = 1)
print(new_graph + labs(
  title = "Relation between Mile per hours and drat",
  subtitle = "Relationship breakdown by gear class",
  caption = "Authors own computation"
))
