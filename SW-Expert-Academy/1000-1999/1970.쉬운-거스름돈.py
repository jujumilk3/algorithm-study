case_count = int(input())

for i in range(1, case_count + 1):
    money = int(input())
    units = [0] * 8
    while money > 9:
        if money >= 50000:
            units[0] = money // 50000
            money = money - units[0] * 50000
        elif money >= 10000:
            units[1] = money // 10000
            money = money - units[1] * 10000
        elif money >= 5000:
            units[2] = money // 5000
            money = money - units[2] * 5000
        elif money >= 1000:
            units[3] = money // 1000
            money = money - units[3] * 1000
        elif money >= 500:
            units[4] = money // 500
            money = money - units[4] * 500
        elif money >= 100:
            units[5] = money // 100
            money = money - units[5] * 100
        elif money >= 50:
            units[6] = money // 50
            money = money - units[6] * 50
        elif money >= 10:
            units[7] = money // 10
            money = money - units[7] * 10
    print('#{}'.format(i))
    print(' '.join(list(map(str, units))))


"""
2 
32850
160             
"""
