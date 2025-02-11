from random import *

dreierPaschGewürfelt = False

tries = 0

while not dreierPaschGewürfelt:
    number1 = randint(1, 6)
    number2 = randint(1, 6)
    number3 = randint(1, 6)
    
    tries += 1

    if number1 == number2 and number2 == number3:
        print(f"Dreier-Pasch mit {number1}en in {tries} Versuchen")
        dreierPaschGewürfelt = True