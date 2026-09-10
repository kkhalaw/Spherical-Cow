import math

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

# get velocities
vxo, vyo = vector_components()

# remaining inputs 
ax = float(input("Acceleration in x: "))
xo = float(input("Initial x position: "))

ay = float(input("Acceleration in y (gravity): "))
yo = float(input("Initial y position: "))

dt = float(input("Time step: "))

# initial conditions
t = 0
x = xo
y = yo

# physics functions 

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

def output(rows):
    # rows should be a list of (t, x, y)

    # compute column widths dynamically
    cols = list(zip(*rows))
    w_t = max(len(str(x)) for x in cols[0])
    w_x = max(len(str(x)) for x in cols[1])
    w_y = max(len(str(x)) for x in cols[2])

    with open("SphericalCowTable.tsv", "w") as f:
        # header
        f.write(f"{'Time':<{w_t}}\t{'Pos. X':<{w_x}}\t{'Pos. Y':<{w_y}}\n")

        # rows
        for t_val, x_val, y_val in rows:
            f.write(f"{t_val:<{w_t}}\t{x_val:<{w_x}}\t{y_val:<{w_y}}\n")

rows = []


while y > 0.001:
    t = time(t, dt)
    x, vx = position(x, vxo, ax, t)
    y, vy = height(y, vyo, ay, t)

    rows.append((round(t,3), round(x,3), round(y,3)))

    print("t =", t)
    print("x =", x, "vx =", vx)
    print("y =", y, "vy =", vy)

output(rows)
print("Table written.")
