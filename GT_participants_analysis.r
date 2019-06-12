setwd("C:/Users/i.dalbo/Desktop/Data_Analysis_Portfolio")
data = read.csv("GT_finishing_part.csv")

# Plot of participant fractions ending Giro, Tour, Vuelta
par(bg = 'lightcyan')
plot(data$Anno,data$GiroN,type="l",main = "Fraction of participants finishing the 3GT (1990-2019), normalized",xlab="Year",ylab="Number of finishing participant",col="pink", lwd=2, ylim=c(0.3,1))
lines(data$Anno,data$TourN,col="gold",lwd=2)
lines(data$Anno,data$VueltaN,col="red",lwd=2)
legend(1990, 0.4, legend=c("Giro", "Tour","Vuelta"),
       col=c("pink", "gold", "red"),lty=1:1, lwd=3, cex=1,text.font=1, bg='lightcyan')

#Correlation analysis of the data
library(corrplot)
norm = data[1:29,(c(6,7,8))]
corrplot(cor(norm))

         