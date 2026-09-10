import math
import matplotlib.pyplot  as plt #plotting library


def calc_force(mass, D = 0, vx= 0,vy = 0):
    Fx = 0
    Fy = mass * 9.81 #gravity = ay
    
    
    D = 4
    dragX =  D * vx**2
    dragY = D * vy**2
    
    Net_dragX = dragX - Fy #Fy = mass * 9.81 
    Net_dragY = dragY - Fy 
    
    if Net_dragX != 0 and Net_dragY != 0:
        return Net_dragX, Net_dragY
    else:
        return Fx, Fy 



#A function to calculate the potential energy at a given instance
#height = new y position
def potential(mass,height):
    PE = mass * 9.81 * height
    return PE
    


#A function to calculate the kinetic energy at a given instance
#speed can be 
def kinetic(mass,vx, vy):
    v = math.sqrt((vx**2)+(vy**2))
    KE = ((mass) * (v)**2)/2
    return KE

#A function to calculate total energy of the system at a given instance
def TotalE(KE, PE):
    total = KE + PE
    return total


##Beginning of the main program

vo =float(input("What is the initial velocity vector? "))
OoO = float(input("What is the angle between the velocity vector and the x-axis? "))


ax = int(input("What is the acceleration in the x direction? "))
xo = int(input("What is the initial position along the x-axis? "))


ay = float(input("What is the acceleration in the y direction (gravity)? "))
yo = float(input("What is the initial position along the y-axis? "))

mass = float(input("What is the mass of the spherical cow? "))


dt = 0.001
t = 0



# Convert angle to radians
theta = math.radians(OoO)


# Initial velocity components
vxo = vo * math.cos(theta)
x = xo


vyo = vo * math.sin(theta)
y = yo


def position (x, vxo, ax, t):
    x = xo + (vxo * t)
    vx = vxo + (ax * t)
    return x , vx


def height (y, vyo, ay, t):
    y = yo - (vyo * t)
    vy = vyo + (ay * t)
    return y , vy


def time (t, dt):
    t = t + dt
    return t


x_positions = []
y_positions = []
time_elapsed = []
KE_values = []
PE_values = []
total_energies = []

net_force_drag = []


while y > 0.001:
    t = time(t, dt)
    x, vx = position(x, vxo, ax, t)
    y, vy = height(y, vyo, ay, t)


    x_positions.append(x)
    y_positions.append(y)
    time_elapsed.append(t)

    net_force = calc_force(mass)
    drag_force = calc_force(mass, D=4, vx=vx, vy=vy)  


    KE = kinetic(mass, vx, vy)  
    PE = potential(mass, y)  
    total_energy = TotalE(KE, PE)

    KE_values.append(KE)
    PE_values.append(PE)
    total_energies.append(total_energy)
    net_force_drag.append((drag_force))

    print("t =", t)
    print("x =", x, "vx =", vx)
    print("y =", y, "vy =", vy)
    print("force =", net_force) #idk if this should be included? it'll probably be 9.81 * 1000 a bunch lol 
    print("drag force =", drag_force)

plt.plot(x_positions, y_positions)
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Trajectory of the Spherical Cow")
plt.show()

plt.plot(time_elapsed, KE_values, label="Kinetic Energy")
plt.xlabel("Time")
plt.ylabel("Kinetic Energy")
plt.title("Kinetic Energy vs. Time")
plt.show()

plt.plot(time_elapsed, PE_values, label="Potential Energy")
plt.xlabel("Time")
plt.ylabel("Potential Energy")
plt.title("Potential Energy vs. Time")
plt.show()

plt.plot(time_elapsed, total_energies, label="Total Energy")
plt.xlabel("Time")
plt.ylabel("Total Energy")
plt.title("Total Energy vs. Time")
plt.show()

plt.plot(time_elapsed, net_force_drag, label="Net Force")
plt.xlabel("Time")
plt.ylabel("Net Force")
plt.title("Net Force With Air Resistance vs. Time")
plt.show()

