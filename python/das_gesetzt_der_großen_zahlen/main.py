from random import randint

rollsAmount = int(input("Wie oft soll Gewürfelt werden?: "))

#data[0] = 1, data[1] = 2 ...
data = [0, 0, 0, 0, 0, 0]

for i in range(0, rollsAmount):
    rolled = randint(1, 6)

    data[rolled - 1] += 1

print("")

for i in range(0, len(data)):
    print(f"Wahrscheinlichkeit für eine {i + 1}: {data[i] / rollsAmount}")