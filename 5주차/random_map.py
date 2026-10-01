import random

for i in range(10):
    for j in range(10):
        if random.randint(0, 1) == 0:
            print(".", end=" ")
        else:
            print("#", end=" ")
    print()
