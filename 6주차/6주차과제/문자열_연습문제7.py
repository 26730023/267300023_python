hour = int(input())
minute = int(input())
if hour < 10:
    hour = "0" + str(hour)
if minute < 10:
    minute = "0" + str(minute)
print(f"{hour}:{minute}")
