case_count = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for case_number in range(1, case_count + 1):
    start_month, start_day, end_month, end_day = list(map(int, input().split()))
    result = 0
    if start_month < end_month:
        result += sum(days[start_month-1:end_month-1])
    result += (end_day - start_day) + 1
    print('#{} {}'.format(case_number, result))


"""
8
3 1 3 31
3 1 3 1
5 5 8 15
7 17 12 24
1 31 2 1
1 1 2 2
1 1 2 1
1 15 2 1 
"""
