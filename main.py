import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

from magnets import solenoid, longstraightwire
from electrics import PointCharge

# Graphing a B field for a slice of a long straight wire

x = np.linspace(-5, 5, 40)
y = np.linspace(-5, 5, 40)

mag1 = longstraightwire(x=0, y=0, current=50)
x,y = np.meshgrid(x,y)

bx, by = mag1.B_fieldstr(x, y)

plt.figure()
color = 2 * np.log(np.sqrt(bx**2 + by**2))
plt.streamplot(x,y, bx, by, color=color, linewidth=1, cmap=plt.cm.coolwarm,
               density=2, arrowstyle='->', arrowsize=1.5)
plt.title("Long Straight Wire B-Field")
plt.show()

# Finding B fields for the inside of a solenoid

sol1 = solenoid(r1=0.0125, r2=0.013, current=50, length=10)
resistivity = 1.68E-8  # Ohm Meter
packing = 0.75
power = 100.0  # watts
x1 = np.linspace(-5, 5, 100)
x2 = x1 + sol1.length
B_fields = np.zeros(100)
G_fac = np.zeros(100)
for i in range(len(B_fields)):
    G_fac[i] = sol1.G_factor(x1=x1[i], x2=x2[i])
    B_fields[i] = sol1.B_fieldsol(power, packing, resistivity, x1=x1[i], x2=x2[i])
    # The B field is everywhere the same inside of the solenoid as expected except for the special case

# Finding the electric field due to the superposition of 2 charges and creating a dipole

PC1 = PointCharge(Q=5, x=20, y=0)
PC2 = PointCharge(Q=-5, x=-20, y=0)

x = np.linspace(-100,100,24)
y = np.linspace(-100,100,24)
x,y = np.meshgrid(x,y)

Ex1, Ey1 = PC1.E_Field(x, y)
Ex2, Ey2 = PC2.E_Field(x, y)
Ex, Ey = (Ex1+Ex2), (Ey1+Ey2)


plt.figure()
color = 2 * np.log(np.sqrt(Ex**2 + Ey**2))
plt.streamplot(x,y, Ex,Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
               density=2, arrowstyle='->', arrowsize=1.5)
plt.plot(20, 0, '-or')
plt.plot(-20, 0, '-ob')
plt.title("Dipole E-Field")
plt.show()