import numpy as np
import matplotlib.pyplot as plt

def dist(x, y):
    return np.sqrt(x**2 + y**2)

N = 1000000
N_int = 0

for i in range(1, N+1):
    x = np.random.uniform(0,1)
    y = np.random.uniform(0,1)
    if(dist(x, y) < 1):
        N_int += 1
        plt.xlim(0,1)
        plt.ylim(0,1)
        plt.scatter(x, y, color = 'green')
    else:
        plt.xlim(0,1)
        plt.ylim(0,1)
        plt.scatter(x, y, color = 'red')

#plotting circle
#theta = np.linspace(0, np.pi / 2, 150)
#radius = 1
#x_c = radius * np.cos(theta)
#y_c = radius * np.sin(theta)
#plt.plot(x_c, y_c, color = "blue")
#plt.show()

pi = 4 * N_int/N
error = np.pi - pi
print("N = %d; pi = %5.10f; error = %5.2e" % (N,pi,error))






