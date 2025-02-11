from random import *

sixesRolled = 0
rolls = 0

while sixesRolled != 5:
    randomNumber = randint(1, 6)

    if randomNumber == 6:
        sixesRolled += 1
    
    rolls += 1

print(f"Rolls: {rolls}")
