def generate_state():
    return ".........0........."

def select_rule(num):
    "Select rule to be used in the simulation"
    RULES = {
    30: {"...": '.', "..0": '0', ".0.": '0', "000": '.',
          ".00": '0', "0..": '0', "0.0": '.', "00.": '.'},
    90: {"...": "0", "..0": ".", ".0.": "0", ".00": ".",
          "0..": ".", "0.0": "0", "00.": ".", "000": "0"},
    110: {"...": '0', "..0": '.', ".0.": '.', ".00": '0',
           "0..": '.', "0.0": '.', "00.": '.', "000": '0'},
    184: {"...": ".", "..0": "0", ".0.": ".", ".00": ".",
           "0..": ".", "0.0": "0", "00.": "0", "000": "0"}
     }
    return RULES[num]
    

def find_neighbors(index, oldstate):
    "Find the neighborhood of a cell based on it's position (index)"
    if index == 0:
        neighbors = oldstate[-1] + oldstate[0] + oldstate[1]
    elif index == len(oldstate) - 1:
        neighbors = oldstate[index - 1] + oldstate[index] + oldstate[0]
    else:
        neighbors = oldstate[index - 1] + oldstate[index] + oldstate[index + 1]
    return neighbors


def evolve(oldstate, n_rule):
    "Evaluate  the evolution of a state, based on the selected rule"
    rule = select_rule(n_rule)
    newstate = ""
    for i in range(len(oldstate)):
        neighbors = find_neighbors(i, oldstate)
        newstate += rule[neighbors]
    return newstate


def simulation(nsteps, n_rule):
    "This function performs the actual simulation returning the history of the system"
    initial_state = generate_state()
    state_history = [initial_state]
    for i in range(nsteps):
        old_state = state_history[-1]
        new_state = evolve(old_state, n_rule)
        state_history.append(new_state)
    return state_history
