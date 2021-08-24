count = 0
for char in input():
    print(char, end='')
    count += 1
    if count >= 10:
        print()
        count = 0
