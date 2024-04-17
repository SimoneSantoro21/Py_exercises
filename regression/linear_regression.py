import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#setting default matplotlib deeplearning style
plt.style.use('./deeplearning.mplstyle')

test_set = pd.read_csv('regression\linear_regression.csv')

x = test_set['X'].to_numpy()
y = test_set['Y'].to_numpy()

plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear regression')
plt.show()




