import numpy as np
import matplotlib.pyplot as plt
import math

def average(list x, y):
    x_sum =  sum()
    return True

# definition of variables, distance btween each molecule, number of branches, number of beads (assuming same number for every branch), coordinates
dist = 0.2
branches = 5
beads = 1000
x = [0]*beads
y = [0]*beads
x_displ = []*(branches)
y_displ = []*branches
colors = ['blue', 'red', 'black', 'green', 'yellow']
#generating ith branch
for j in range(branches):
 
    #generating single beads for that branch
    for i in range(beads -1):
        theta = np.random.uniform(0, 2*np.pi)
        x[i+1] = x[i] + dist * math.cos(theta)
        y[i+1] = y[i] + dist * math.sin(theta)
        x_displ[j] += x[i+1]
        y_displ[j] += y[i+1]
        #plt.plot(x, y, color = colors[j])



#plt.show()




