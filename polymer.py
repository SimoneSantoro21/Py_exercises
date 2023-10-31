import numpy as np
import matplotlib.pyplot as plt
import math

def average(list R[][]):
    return True

# definition of variables, distance btween each molecule, number of branches, number of beads (assuming same number for every branch), coordinates
dist = 0.2
branches = 5
beads = 1000
x = [0]*beads
y = [0]*beads
R = [(0, 0)]*(branches)
colors = ['blue', 'red', 'black', 'green', 'yellow']
#generating ith branch
for j in range(branches):
    x_displ = 0
    y_displ = 0

    #generating single beads for that branch
    for i in range(beads -1):
        theta = np.random.uniform(0, 2*np.pi)
        x[i+1] = x[i] + dist * math.cos(theta)
        y[i+1] = y[i] + dist * math.sin(theta)
        x_displ += x[i+1]
        y_displ += y[i+1]
        #plt.plot(x, y, color = colors[j])

    R[j] = (x_displ, y_displ)
    print(j)
    print(R)


#plt.show()




