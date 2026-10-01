import matplotlib.pyplot as plt
import random

values = [random.randint(0, 5) for i in range(600)]

faces = [1, 2, 3, 4, 5, 6]
rolls = [0, 0, 0, 0, 0, 0]

for x in values:
    rolls[x] = rolls[x] + 1

plt.bar(faces, rolls)
plt.show()
