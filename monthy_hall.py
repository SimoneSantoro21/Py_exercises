import numpy as np
import matplotlib.pyplot as plt


N = 10000000
win_no_switch = 0
win_switch = 0

for i in range(N):
    doors = ['Door 1', 'Door 2', 'Door 3']

    first_choice = np.random.choice(doors)
    winning_door = np.random.choice(doors)
    opened_door = list(set(doors) - set([first_choice, winning_door]))[0]
    other_door = list(set(doors) - set([first_choice, opened_door]))[0]

    if(first_choice == winning_door):
        win_no_switch += 1

    first_choice = other_door
    if(first_choice == winning_door):
        win_switch += 1


print("By switching, the measured probability of success is p_switch = ", win_switch / N)
print("By keeping the first choice, the measured probability of success is p_no_switch = ", win_no_switch / N)