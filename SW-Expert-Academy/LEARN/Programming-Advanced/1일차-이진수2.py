case_count = int(input())

for t in range(case_count):
    answer = ''
    number = float(input())
    sub_num = 1
    for _ in range(12):
        sub_num *= 0.5
        if number - sub_num >= 0:
            answer += '1'
            number -= sub_num
            if not number:
                break
        else:
            answer += '0'
    if number: answer = 'overflow'
    print('#{} {}'.format(t+1, answer))
