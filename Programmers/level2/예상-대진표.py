from math import ceil


def solution(n, a, b):
    answer = 1
    if b < a:
        a, b = b, a
    while n > 2:
        if a - b == -1 and a % 2 != 0:
            break
        a = ceil(a/2)
        b = ceil(b/2)
        n = n // 2
        answer += 1
    return answer


print(solution(8, 4, 7))
print(solution(8, 4, 7))
print(solution(8, 1, 2))
print(solution(8, 2, 1))
print(solution(8, 1, 8))
print(solution(8, 1, 3))
print(solution(8, 4, 5))
