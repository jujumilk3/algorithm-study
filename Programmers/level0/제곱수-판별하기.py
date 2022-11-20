def solution(n):
    return 1 if (n ** 0.5) % 1 == 0 else 2


assert solution(144) == 1
assert solution(976) == 2
