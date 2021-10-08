unit_count, money = map(int, input().split())
units = [int(input()) for _ in range(unit_count)]
count = 0
units.sort(reverse=True)

while money:
    for unit in units:
        if money >= unit:
            count += money // unit
            money -= unit * (money // unit)
            break

print(count)
