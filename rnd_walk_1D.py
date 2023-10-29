import numpy as np
import matplotlib.pyplot as plt

#Number of steps, displacement of each step and original position
N_steps = 10000
d = 1
y = [0]*(N_steps)
x = [i for i in range(0, N_steps)]

for i in range(1, N_steps):
    dir = np.random.uniform(0, 1)
    if(dir >= 0.5):
        y[i] = y[i-1]+1
    else:
        y[i] = y[i-1]-1

plt.xlim(0, N_steps)
plt.ylim(-max(max(y), np.absolute(min(y))), max(max(y), np.absolute(min(y))))

plt.plot(x, y, color = "blue")
plt.show()

