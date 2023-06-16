def solution(num_list):
    answer = 0
    for num in num_list:
        while num != 1:
            if num % 2 == 0:
                num = num // 2
                answer += 1
            else:
                num = (num - 1) // 2
                answer += 1
    return answer
