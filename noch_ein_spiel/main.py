from random import randint

class container:
    def __init__(self, capacity: int, name: str, storedAmount: int = 0):
        self.capacity = capacity
        self.storedAmount = storedAmount
        self.name = name

    def addWine(self, amount):
        if amount > self.capacity:
            self.storedAmount += self.getLeftSpace()
        self.storedAmount += amount

    def fillOther(self, other):
        if self.storedAmount > other.getLeftSpace():
            transferAmount = other.getLeftSpace()
        else:
            transferAmount = self.storedAmount

        self.storedAmount -= transferAmount
        other.storedAmount += transferAmount

    def getLeftSpace(self):
        return self.capacity - self.storedAmount

barrrel = container(8, "Fass", 8)
jug1 = container(5, "5-Liter Krug")
jug2 = container(3, "3-Liter Krug")

vessels = [barrrel, jug1, jug2]

attempts = 0

while True:
    vessel1 = vessels[randint(0, 2)]
    vessel2 = vessels[randint(0, 2)]


    #Check if the vessels are the same
    while vessel1 == vessel2:
        vessel2 = vessels[randint(0, 2)]

    #Check if the vessels are empty and the second vessel has spacde left
    if (vessel1.storedAmount == 0 and vessel2.storedAmount == 0) or vessel2.getLeftSpace() == 0:
        continue
    
    attempts += 1
    if vessel1.storedAmount == 0:
        vessel2.fillOther(vessel1)
    else:
        vessel1.fillOther(vessel2)

    print(f"Filled {vessel1.name} into {vessel2.name}")
    print(f"Fass: {vessels[0].storedAmount}")
    print(f"5-Liter Krug: {vessels[1].storedAmount}")
    print(f"3-Liter Krug: {vessels[2].storedAmount}")
    print("")

    if vessels[0].storedAmount == 4 or vessels[1].storedAmount == 4 or vessels[2].storedAmount == 4:
        print(f"Vesuche: {attempts}")
        break
