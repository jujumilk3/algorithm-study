case_count = int(input())

for i in range(1, case_count + 1):
    numbers_count = int(input())
    numbers = list(map(int, input().split()))
    result = max(numbers) - min(numbers)
    print('#{} {}'.format(i, result))


# Input
"""
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
"""
