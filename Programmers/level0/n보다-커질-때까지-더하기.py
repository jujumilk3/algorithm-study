def solution(numbers, n):
    answer = 0
    idx = 0
    while answer <= n:
        answer += numbers[idx]
        idx += 1
    return answer
