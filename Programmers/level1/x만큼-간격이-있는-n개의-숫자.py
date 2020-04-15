def solution(x, n):
    answer = []
    for i in range(1, n + 1):
        answer.append(x * i)
    return answer


print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))
