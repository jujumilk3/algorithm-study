case_count = int(input())

for case_number in range(1, case_count + 1):
    time = sum(list(map(int, input().split())))
    time = time if time < 24 else time - 24
    print('#{} {}'.format(case_number, time))

"""
3
1 9
7 17
23 23 
"""
