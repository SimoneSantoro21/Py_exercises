import numpy as np

N = 1
states = ["State 1", "State 2", "State 3"]
particles = np.zeros(N)
particles = states[0]

#transition matrix 
pi = [[1/2, 1/3, 1/2],
      [1/4, 0, 1/2],
      [1/4, 2/3, 0]]

#definition of transition function
def transition(init_condition, transition_matrix):
    p = np.random.uniform(0, 1)
    if (init_condition == states[0]):
        if (p <= 0.5):
            new_state = states[0]
        if ( p > 0.5 and p <= 0.75):
            new_state = states[1]
        if (p > 0.75 and p <= 1):
            new_state = states[2]
    if (init_condition == states[1]):
        if (p <= 0.33):
            new_state = states[0]
        if ( p > 0.33 and p <= 1):
            new_state = states[2]
    if (init_condition == states[2]):
        if (p <= 0.5):
            new_state = states[0]
        if ( p > 0.5 and p <= 1):
            new_state = states[1]



