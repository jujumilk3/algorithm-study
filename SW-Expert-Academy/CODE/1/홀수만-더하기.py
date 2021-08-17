case_count = int(input())

numbers_lists = []
for i in range(case_count):
    input_numbers = list(map(int, input().split()))
    for j in range(len(input_numbers)):
        if input_numbers[j] % 2 == 0:
            input_numbers[j] = 0
    numbers_lists.append(input_numbers)

for i in range(case_count):
    print('#{} {}'.format(i+1, sum(numbers_lists[i])))
