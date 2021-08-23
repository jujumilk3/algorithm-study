case_count = int(input())

for i in range(1, case_count + 1):
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(i, max(numbers)))


"""
3 
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1   
"""
