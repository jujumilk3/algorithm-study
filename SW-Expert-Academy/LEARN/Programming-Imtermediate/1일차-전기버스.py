case_count = int(input())

for i in range(1, case_count + 1):
    K, N, M = list(map(int, input().split()))
    course = [0 for x in range(N)]
    stations = list(map(int, input().split()))
    for station in stations:
        course[station] = 1
    print(course)
    current_fuel = K+1
    run_distance = K-1
    for j in range(N-1):
        current_fuel -= 1
        print(j, course[j], current_fuel)


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
