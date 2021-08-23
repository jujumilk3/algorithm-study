case_count = int(input())

for i in range(1, case_count + 1):
    left, right = input().split()
    left = int(left)
    right = int(right)
    if left > right:
        result = '>'
    elif left < right:
        result = '<'
    else:
        result = '='
    print('#{} {}'.format(i, result))


# Input
"""
3
3 8 
7 7 
369 123
"""
