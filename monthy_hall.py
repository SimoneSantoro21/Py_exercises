import numpy as np
import matplotlib.pyplot as plt


def switch(chosen_door, other_door, bool):
    if(bool == True):
        a = chosen_door
        b = other_door
        chosen_door=b
        other_door=a
    #return True

def open_a_door():
    return 

doors = ['Door 1', 'Door 2', 'Door 3']

first_choice = np.random.choice(doors)
winning_door = np.random.choice(doors)
opened_door = list(set(doors) - set([first_choice, winning_door]))[0]
other_door = list(set(doors) - set([first_choice, opened_door]))[0]

print("chosen door = ", first_choice)
print("Opened door = ", opened_door)
print("Other door = ", other_door)
print("winning door =", winning_door)


#
#switch(first_choice, winning_door, True)
#
#print("chosen door =", first_choice)
#print("winning door =", winning_door)