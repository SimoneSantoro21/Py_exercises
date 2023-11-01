import numpy as np
import matplotlib.pyplot as plt

#define variables
m = 1 #kg
g = 9.81 #m/s^2
h0 = 500 #m
v0 = (5 , 0) #m/s
T = 10 #s

#define timesteps and
dt = 1/50 * T
N = int(T / dt)

#define positions and forces
r = np.zeros((N+1, 2))
r[0] = (0, h0)

v = np.zeros((N+1, 2))
v[0] = v0

f = np.zeros((N+1, 2))
f[:] = np.array([0, - m * g])

#update dynamics
for n in range(N):
    v[n+1] = v[n] + (f[n]/m) * dt
    r[n+1] = r[n] + v[n+1] * dt
    plt.scatter(r[n][0], r[n][1])

plt.show()