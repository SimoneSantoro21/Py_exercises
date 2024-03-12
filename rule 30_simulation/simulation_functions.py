def generate_state():
    return ".........0........."

def evolve(oldstate):
    return oldstate


def simulation(nsteps):
    "This function performs the actual simulation returning the history of the system"
    initial_state = generate_state()
    state_history = [initial_state]
    for i in range(nsteps):
        old_state = state_history[-1]
        new_state = evolve(old_state)
        state_history.append(new_state)
    return state_history
