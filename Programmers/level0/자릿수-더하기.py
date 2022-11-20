def solution(n):
    return sum(map(int, (str(n))))


assert solution(1234) == 10
assert solution(930211) == 16
