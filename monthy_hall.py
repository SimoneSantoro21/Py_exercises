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

doors = ['a', 'b', 'c']

choice = doors[np.random.randint(1, 4) - 1]
winning_door = doors[np.random.randint(1, 4) - 1]

print("chosen door =", choice)
print("winning door =", winning_door)

switch(choice, winning_door, True)

print("chosen door =", choice)
print("winning door =", winning_door)