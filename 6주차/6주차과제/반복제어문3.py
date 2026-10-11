a, b = input().split()

start = ord(a)
end = ord(b)

if start <= end:
    for i in range(start, end + 1):
        print(chr(i), end=" ")
else:
    for i in range(start, end - 1, -1):
        print(chr(i), end=" ")
