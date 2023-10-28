import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

def gaussian(x, m, std):
    term1= 1/np.sqrt(2*np.pi*std**2)
    term2= np.exp(-((x-m)**2)/(2*std**2))
    return term1*term2

#define binomial variable r extracted of n trials, w/ probability p, repeted size times
n = 100
p = 0.5
size = 1000
r = np.random.binomial(n, p, size)
print(r)

#create histogram of occurencies 
plt.hist(r, bins=n, range=(0,n), density = True, align='left', color="green", rwidth=0.8)

#plotting binomial distribution
x = [i for i in range(n+1)]
y = binom.pmf(x, n, p)
plt.plot(x, y, "--", color="red", lw=4)

xg = np.linspace(0, n, 1000)
mean = n*p
std = np.sqrt(n* p * (1-p))
yg = gaussian(xg, mean, std)
plt.plot(xg, yg, color="blue")

plt.show()