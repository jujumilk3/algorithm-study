string = input()
split = string.split()
x, y, z = int(split[0]), int(split[1]), int(split[2])
benefit = z - y
print((x // benefit) + 1 if benefit > 0 else -1)
