a = []

while True:
    n = int(input())

    if n == 0:
        break

    a.append(n)

for i in range(1, len(a), 2):
    print(a[i], end=" ")
