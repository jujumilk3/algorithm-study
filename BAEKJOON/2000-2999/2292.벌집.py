room_number = int(input())

number = 1
count = 0

while number < room_number:
    count += 1
    number = number + (count * 6)

print(count+1)
