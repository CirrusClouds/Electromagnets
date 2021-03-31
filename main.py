import numpy as np
import matplotlib.pyplot as plt
from magnets import solenoid, longstraightwire

# Graphing a B field for a slice of a long straight wire

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)


mag1 = longstraightwire(x=0, y=0, current=50)
B_fields = mag1.B_fieldstr(x, y)
plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(x, y, B_fields, 50, cmap='binary')
ax.view_init(30, 65)
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
