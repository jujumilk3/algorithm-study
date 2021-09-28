case_count = int(input())

for case_number in range(1, case_count + 1):
    A, B = list(map(int, input().split()))
    answer = -1 if A > 9 or B > 9 else A * B
    print('#{} {}'.format(case_number, answer))

"""
4
2 5
5 10
10 10
9 9 
"""
