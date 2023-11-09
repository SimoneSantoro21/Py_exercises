import numpy as np

#defining variables 
N = 1000000                                  #number of iterations per particle
N_particles = 10000                             #number of particles
states = ["State 1", "State 2", "State 3"]  #Possible states
n_state_1 = 0                               #
n_state_2 = 0                               #outcome counters
n_state_3 = 0                               #
trajectory = []                    #trajectory of the outcomes, not differentiated by the particle
particles = [[]*N]*N_particles 

#transition matrix 
pi = [[1/2, 1/3, 1/2],
      [1/4, 0, 1/2],
      [1/4, 2/3, 0]]

#definition of transition function
def transition(init_condition, transition_matrix):
    p = np.random.uniform(0, 1)
    if (init_condition == states[0]):
        if (p <= pi[0][0]):
            new_state = states[0]
        if ( p > pi[0][0] and p <= pi[0][0] + pi[1][0]):
            new_state = states[1]
        if (p > pi[0][0] + pi[1][0] and p <= 1):
            new_state = states[2]
    if (init_condition == states[1]):
        if (p <= pi[0][1]):
            new_state = states[0]
        if (p > pi[0][1] and p <= pi[0][1] + pi[1][1]):
            new_state = new_state
        if (p > pi[0][0] + pi[1][0] and p <= 1):
            new_state = states[2]
    if (init_condition == states[2]):
        if (p <= pi[0][2]):
            new_state = states[0]
        if (p > pi[0][2] and p <= pi[0][2] + pi[1][2]):
            new_state = states[1]
        if (p > pi[0][2] + pi[1][2] and p <= 1):
            new_state = new_state
    return new_state

#for cyccle for different particles, define a particles list etc
for particle in range(N_particles):
    particles[particle][0] = np.random.choice(states)
    trajectory[particle] = particles[particle][0]
    for step in range(N):
        trajectory.append(transition(particles[particle][step], pi))
        if (trajectory[step] == states[0]):
            n_state_1 += 1
        if (trajectory[step] == states[1]):
            n_state_2 += 1
        if (trajectory[step] == states[2]):
            n_state_3 += 1


ro_eq = [n_state_1 / N, n_state_2 / N, n_state_3 / N]

print("At equilibrium, probability vector ro = ", ro_eq,
       "\n With number iteration N = ", N,
       "\n and number of particles N_particles = ", N_particles)
    