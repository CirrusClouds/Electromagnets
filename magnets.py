import numpy as np

# Constants
permeability = (1.257 * 10**-6)  # in free space
Me = (9.11 * 10**-31)  # Mass of electron
qe = -(1.60 * 10**-19)  # Charge of electron


class longstraightwire:
    def __init__(self, x, y, current):
        self.x = x
        self.y = y
        self.current = current


    def B_fieldstr(self, x, y):
        B = np.zeros((100, 100))
        for i in range(len(x)):
            for j in range(len(y)):
                distance = np.sqrt((x[i] - self.x)**2 + (y[j] - self.y)**2)
                B[i,j] = (permeability * self.current) / (2 * np.pi * distance)

        return B


class solenoid:
    def __init__(self, r1, r2, current, length):
        self.r1 = r1  # Inner radius
        self.r2 = r2  # Outer radius
        self.current = current
        self.length = length

    def G_factor(self, x1=0.0, x2=0.0):
        g = (x1 + x2) / 2*self.r1
        a = self.r2 / self.r1
        b = self.length / (2*self.r1)

        if g == 0.0:
            coeff = np.sqrt((b / 2*np.pi*(a**2 - 1)))
            log = np.log((a + np.sqrt(a**2 + b**2)) / (1 + np.sqrt(1 + b**2)))
            G = coeff * log
        else:
            coeff = np.sqrt(1 / (8*np.pi*b*(a**2 -1)))
            part1 = (g+b) * np.log((a + np.sqrt(a**2 + (g+b)**2))/(1 + np.sqrt(1 + (g+b)**2)))
            part2 = (g-b) * np.log((a + np.sqrt(a**2 + (g-b)**2))/(1 + np.sqrt(1 + (g-b)**2)))
            G = coeff * (part1 - part2)
        return G

    def B_fieldsol(self, power, cross, resistivity, x1=0.0, x2=0.0):
        roots = np.sqrt((power * cross) / (resistivity * self.r1))
        B = permeability * roots * solenoid.G_factor(self, x1, x2)
        return B

# Next: Circular loop
