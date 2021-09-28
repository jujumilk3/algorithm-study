case_count = int(input())

for case_number in range(1, case_count + 1):
    length = int(input())
    numbers = list(map(int, input().split()))
    minmax = [min(numbers), max(numbers)]
    answer = 0
    for i in range(1, length-1):
        if numbers[i-1] < numbers[i] < numbers[i+1] or numbers[i-1] > numbers[i] > numbers[i+1]:
            answer += 1
    print('#{} {}'.format(case_number, answer))

"""
2
3
1 3 2
5
1 3 5 4 2 
"""
