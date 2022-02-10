rest = 1000 - int(input())
units = [500, 100, 50, 10, 5, 1]
count = 0
while True:
    for unit in units:
        if rest >= unit:
            rest -= unit
            count += 1
            break
    if rest == 0:
        break
print(count)
