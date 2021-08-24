x = int(input())
y = int(input())
location = 0
if x * y > 0:
    location = 1 if x > 0 else 3
else:
    location = 2 if x < 0 else 4
print(location)
