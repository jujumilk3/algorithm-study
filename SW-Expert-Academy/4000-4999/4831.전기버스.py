case_count = int(input())

for i in range(1, case_count + 1):
    K, N, M = list(map(int, input().split()))
    course = [0 for x in range(N+1)]
    stations = list(map(int, input().split()))
    for station in stations:
        course[station] = 1
    print(K, N, M)
    print(course)
    current_fuel = K+1
    for j in range(N+1):
        current_fuel -= 1
        print(j, course[j], current_fuel)
        if course[j] and current_fuel == 0:
            print('연료 주입 1')
            current_fuel += K
        elif course[j] and not sum(course[j: j+current_fuel-2]):
            print('남은 코스에 주유소 몇개?', sum(course[j:j+current_fuel-1]))
            print('연료 주입 2')
            current_fuel += K
        print('남은 코스에 주유소 몇개?', sum(course[j:j+current_fuel-1]))
        print()
    print()
    print()
    print()
    print()



# Input
"""
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17
"""
