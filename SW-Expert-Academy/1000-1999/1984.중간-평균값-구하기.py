case_count = int(input())

for i in range(1, case_count + 1):
    numbers = list(map(int, input().split()))
    del numbers[numbers.index(max(numbers))]
    del numbers[numbers.index(min(numbers))]
    print('#{} {}'.format(i, round(sum(numbers)/len(numbers))))
