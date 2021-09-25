case_count = int(input())

for case_number in range(1, case_count + 1):
    people = int(input())
    distances = list(map(abs, list(map(int, input().split()))))
    closest = min(distances)
    print('#{} {} {}'.format(case_number, closest, distances.count(closest)))

"""
2
2
-100 100
3
-5 -1 3
"""
