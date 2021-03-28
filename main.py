import numpy as np


# Constants
permeability = (1.257 * 10**-6)
Me = (9.11 * 10**-31)
qe = -(1.60 * 10**-19)

class magnet:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class longstraightwire(magnet):
    def __init__(self, x, y, z, current):
        self.current = current
        super().__init__(x, y, z)


    def B_field(self, position0):
        currentvector = np.array([0, 0, 1])
        distance = np.sqrt((position0[0] - self.x)**2 + (position0[1] - self.y)**2)
        B = (permeability * self.current) / (2 * np.pi * distance)
        vecnorm = np.array([(position0[1] * currentvector[2] - position0[2] * currentvector[1]), (position0[0] * currentvector[2] - position0[2] * currentvector[0]), (position0[0] * currentvector[1] - position0[1] * currentvector[0])])
        return B, vecnorm

    def MagneticForce(self, B, vecnorm, charge, velocity):
        angleBv = np.arccos(vecnorm * velocity)
        MF = B * charge * velocity * np.sin(angleBv)
        return MF


class Mover:
    def __init__(self, position0, v0, mass, charge):
        self.position0 = position0
        self.v0 = v0
        self.mass = mass
        self.charge = charge

    def EulerMethod(self, mag):
        N = 10
        timestep = 0.01
        N_max = int(N / timestep)
        position = np.zeros((N_max, 3))
        v = np.zeros((N_max,3))
        f = np.zeros((N_max,3))
        a = np.zeros((N_max,3))
        time = np.arange(1, N+1, timestep)

        position[0] = self.position0
        v[0] = self.v0

        for i in range(1,N_max):
            B = mag.B_field((position[i-1]))[0]
            vecnorm = mag.B_field((position[i-1]))[1]
            f[i-1] = mag.MagneticForce(B, vecnorm, self.charge, v[i-1])
            a[i-1] = f[i-1] / self.mass
            v[i] = v[i-1] + timestep * a[i-1]
            position[i] = position[i-1] + timestep * v[i]

        return time, position, a


mag1 = longstraightwire(x=0,y=0,z=0,current=1000)
electron = Mover(np.array([20, -20, 0]), np.array([40, 50, 0]), mass=Me, charge=qe)
print(mag1.B_field(electron.position0))
print(mag1.MagneticForce(mag1.B_field(electron.position0), Me, qe, electron.v0))