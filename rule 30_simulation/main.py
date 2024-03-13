import simulation_functions as func

nsteps = 100
rule = 30
history = func.simulation(nsteps, rule)
for i in range(len(history)-1):
    print(history[i])