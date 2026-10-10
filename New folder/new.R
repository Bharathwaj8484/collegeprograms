# Get the library.  
library(plotrix)

# Create data for the graph.   
x <-	c(21, 62, 10,53)
lbl <-	c("Nashik","Aurangabad","Navi Mumbai","Nagpur")
png(file = "3d_pie_chart.png")   
# Plot the chart.
pie3D(x,labels = lbl,explode = 0.1, main = "Pie Chart of  Countries ")

dev.off()
