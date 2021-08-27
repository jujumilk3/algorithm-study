case_count = int(input())

for i in range(1, case_count + 1):
    number = int(input())
    answer = 0
    for j in range(1, number+1):
        if j % 2 == 0:
            answer -= j
        else:
            answer += j
    print('#{} {}'.format(i, answer))
