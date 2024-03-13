def generate_state():
    return ".........0........."

def select_rule(num):
    "Select rule to be used in the simulation"
    RULES = {
    30: {"...": '0', "..0": '0', ".0.": '0', "000": '0',
          ".00": '.', "0..": '.', "0.0": '.', "00.": '.'},
    90: {"...": "0", "..0": ".", ".0.": "0", ".00": ".",
          "0..": ".", "0.0": "0", "00.": ".", "000": "0"},
    110: {"...": '0', "..0": '.', ".0.": '.', ".00": '0',
           "0..": '.', "0.0": '.', "00.": '.', "000": '0'},
    184: {"...": ".", "..0": "0", ".0.": ".", ".00": ".",
           "0..": ".", "0.0": "0", "00.": "0", "000": "0"}
     }
    
    return RULES.get(num)
    

def evolve(oldstate):
    "Evaluate  the evolution of a state, based on the selected rule"
    newstate = ""
    return newstate


def simulation(nsteps, n_rule):
    "This function performs the actual simulation returning the history of the system"
    initial_state = generate_state()
    rule = select_rule(n_rule)
    state_history = [initial_state]
    for i in range(nsteps):
        old_state = state_history[-1]
        new_state = evolve(old_state)
        state_history.append(new_state)
    return state_history
