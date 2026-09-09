import math

vo = float(input("What is the initial velocity vector?"))
ang = float(input("What is the angle between the velocity vector & the x-axis?"))


ax = float(input("What is the acceleration in the x direction?"))
xo = float(input("What is the inital position along the x-axis?"))

ay = float(input("What is the acceleration in the y direction?"))
yo = float(input("What is the initial position along the y-axis?"))
  
  
#Step-size 
dt = 0.001
t = 0

#Convert angle from degrees to radians
theta = math.radians(ang)

#Calc initial velocity components
vxo= vo * math.cos(theta)
x = xo


vyo = vo * math.sin(theta)
y = yo

while y > 0.001:
    x = xo + (vxo * t)
    vx = vxo + (ax * t)
    y = yo - (vyo * t)
    vy = vyo + (ay * t)
    t = t + dt
    print( f"New time: {t} , New X pos: {x}, New X velocity : {vx}, New Y pos: {y}, New Y velocity: {vy}.")