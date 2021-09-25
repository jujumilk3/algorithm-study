case_count = int(input())

for case_number in range(1, case_count + 1):
    info = list(map(int, input().split()))
    A = info[0] * info[4]
    B_used = 0
    if info[4] > info[2]:
       B_used = (info[4] - info[2]) * info[3]
    B = info[1] + B_used
    print('#{} {}'.format(case_number, min(A, B)))

"""
2
9 100 20 3 10
8 300 100 10 250
"""
