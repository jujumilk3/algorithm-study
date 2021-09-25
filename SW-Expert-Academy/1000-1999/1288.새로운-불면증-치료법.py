case_count = int(input())

for case_number in range(1, case_count + 1):
    N = int(input())
    number_collected = set()
    current_sheep_number = 0
    while len(number_collected) < 10:
        current_sheep_number += N
        number_collected = number_collected | set(str(current_sheep_number))
    print('#{} {}'.format(case_number, current_sheep_number))

"""
5
1
2
11
1295
1692
"""
