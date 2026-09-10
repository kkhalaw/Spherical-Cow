mport math
import matplotlib.pyplot as plt

# ------------------ FORCE & ENERGY FUNCTIONS ------------------

def calc_force(mass, D=0, vx=0, vy=0):
    Fx = 0
    Fy = mass * 9.81  # gravity

    dragX = D * vx**2
    dragY = D * vy**2

    Net_dragX = dragX
    Net_dragY = dragY

    return Net_dragX, Net_dragY


def potential(mass, height):
    return mass * 9.81 * height


def kinetic(mass, vx, vy):
    v = math.sqrt(vx**2 + vy**2)
    return 0.5 * mass * v**2


def TotalE(KE, PE):
    return KE + PE


# ------------------ VELOCITY INPUT FUNCTIONS ------------------

def vector():
    vo = float(input("Initial velocity magnitude: "))
    OoO = float(input("Angle above x-axis: "))
    theta = math.radians(OoO)
    return vo * math.cos(theta), vo * math.sin(theta)


def components():
    vxo = float(input("Initial velocity in x: "))
    vyo = float(input("Initial velocity in y: "))
    return vxo, vyo


def vector_components():
    request = input("Velocity vector type 'vector' or 'component': ")
    if "vector" in request:
        return vector()
    elif "component" in request:
        return components()
    else:
        print("Please type either 'vector' or 'component'")
        return vector_components()


# ------------------ GET USER INPUT ------------------

vxo, vyo = vector_components()

ax = float(input("Acceleration in x: "))
xo = float(input("Initial x position: "))

ay = float(input("Acceleration in y (gravity): "))
yo = float(input("Initial y position: "))

mass = float(input("Mass of the spherical cow: "))

dt = float(input("Time step: "))

# ------------------ INITIAL CONDITIONS ------------------

t = 0
x = xo
y = yo

# ------------------ MOTION FUNCTIONS ------------------

def position(x, vxo, ax, t):
    x = xo + vxo * t
    vx = vxo + ax * t
    return x, vx


def height(y, vyo, ay, t):
    y = yo - vyo * t   # keeping YOUR physics model
    vy = vyo + ay * t
    return y, vy


def time(t, dt):
    return t + dt


# ------------------ DATA STORAGE ------------------

x_positions = []
y_positions = []
time_elapsed = []
KE_values = []
PE_values = []
total_energies = []
net_force_drag = []

rows = []

# ------------------ SIMULATION LOOP ------------------

while y > 0.001:
    t = time(t, dt)
    x, vx = position(x, vxo, ax, t)
    y, vy = height(y, vyo, ay, t)

    rows.append((round(t,3), round(x,3), round(y,3)))

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
    net_force_drag.append(drag_force[0])  # store X drag only for plotting

    print("t =", t)
    print("x =", x, "vx =", vx)
    print("y =", y, "vy =", vy)
    print("force =", net_force)
    print("drag force =", drag_force)


# ------------------ OUTPUT TABLE ------------------

def output(rows):
    cols = list(zip(*rows))
    w_t = max(len(str(x)) for x in cols[0])
    w_x = max(len(str(x)) for x in cols[1])
    w_y = max(len(str(x)) for x in cols[2])

    with open("SphericalCowTable.tsv", "w") as f:
        f.write(f"{'Time':<{w_t}}\t{'Pos. X':<{w_x}}\t{'Pos. Y':<{w_y}}\n")
        for t_val, x_val, y_val in rows:
            f.write(f"{t_val:<{w_t}}\t{x_val:<{w_x}}\t{y_val:<{w_y}}\n")

output(rows)
print("Table written.")

# ------------------ PLOTS ------------------

plt.plot(x_positions, y_positions)
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Trajectory of the Spherical Cow")
plt.show()

plt.plot(time_elapsed, KE_values)
plt.xlabel("Time")
plt.ylabel("Kinetic Energy")
plt.title("Kinetic Energy vs. Time")
plt.show()

plt.plot(time_elapsed, PE_values)
plt.xlabel("Time")
plt.ylabel("Potential Energy")
plt.title("Potential Energy vs. Time")
plt.show()

plt.plot(time_elapsed, total_energies)
plt.xlabel("Time")
plt.ylabel("Total Energy")
plt.title("Total Energy vs. Time")
plt.show()

plt.plot(time_elapsed, net_force_drag)
plt.xlabel("Time")
plt.ylabel("Drag Force (X)")
plt.title("Drag Force vs. Time")
plt.show()

