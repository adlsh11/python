setwd("path/to/project/folder")
install.packages("ggplot2")
library("ggplot2")
input_data <- read.table("height.csv", sep=",", header=TRUE)
attach(input_data)
ggplot(input_data, aes(x,y)) + geom_point() + geom_smooth(method="lm")
lm <- lm(y~x)
predicted_heights <- predict(lm, data.frame(x), interval="predict")
predicted_heights[0:6]
y[0:6]
summary(lm)$r.squared
detach(input_data)