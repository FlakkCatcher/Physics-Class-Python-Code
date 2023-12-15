import math
#That's to get the math functions running properly

###########################
length = 1      ###########
time = 2.02     ###########
###########################
#You put in your measurements for the above variables

Pendulum_Period = 6.28318*(math.sqrt(length/9.8))
Pendulum_Length = ((time/6.28318)**2)*9.8
#This is the background code that contains our equations

print("The Period of the pendulum is:",round(Pendulum_Period, 3),"seconds")
print("The length of the pendulum is:",round(Pendulum_Length, 3),"meters")
#Look down into the Terminal after you run this to get your answers!!