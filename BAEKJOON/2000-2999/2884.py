x = str(input())
hour = int(x.split()[0])
minute = int(x.split()[1])

if minute > 45:
    minute -= 45
else:
    hour -= 1
    minute = 60 + minute - 45

if minute > 59:
    minute -= 60
    hour += 1

if hour < 0:
    hour = 23

print(hour, minute)
