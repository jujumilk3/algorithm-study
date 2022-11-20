def solution(n, t):
    return n * (2 ** t)


assert solution(2, 10) == 2048
assert solution(7, 15) == 229376
