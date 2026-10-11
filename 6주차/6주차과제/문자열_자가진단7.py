hour, minute = input().split()
hour = int(hour)
if hour >= 12:
    ampm = "PM"
    if hour >= 13:
        hour = hour - 12
else:
    ampm = "AM"
hour = str(hour)
if len(hour) == 1:
    hour = "0" + hour
if len(minute) == 1:
    minute = "0" + minute
print(hour, ":", minute, ampm)
