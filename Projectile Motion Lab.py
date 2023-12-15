import math
#This is to to get the math functions working properly

#########################
mass = 1            #####
time= 2.00          #####
release = 0.63      #####
y_init = 4.317      #####
y_final = 0         #####
x_init = 0          #####
x_final = 28.09     #####
#########################
#type in your measurements into their respective places above

x_velocity = x_final / time
y_velocity = (y_final-y_init+(4.9*time**2))/time
total_velocity = math.sqrt(x_velocity**2 + y_velocity**2)
shot_angle = math.degrees(math.acos(x_velocity/total_velocity))
acceleration = total_velocity/release
force = acceleration*mass
#This is the background code to run the equations

print("Horizontal Velocity= ", round(x_velocity, 2), "m/s")
print("Vertical Velocity =", round(y_velocity, 2), "m/s")
print ("Total Velocity =", round(total_velocity, 2), "m/s")
print("Angle of Release =", round(shot_angle, 2), "degrees")
print("Initial Acceleration =", round(acceleration, 2), "m/s^2")
print("Throw Force =", round(force, 2), "N")