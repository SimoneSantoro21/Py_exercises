import numpy as np
import matplotlib.pyplot as plt

N = 1000
rolls = [0, 0, 0, 0, 0, 0]
x = [i for i in range (1, 7)]

for i in range(0, N):
    r = np.random.randint(1, 7)
    rolls[r-1] += 1
    plt.xlim(0, 7)
    plt.bar(x, rolls, color = "blue")
    plt.pause(0.05)

#plt.bar(x, rolls, color = "blue")
plt.hlines(N/6, 0, 8, colors="red")
plt.show()
