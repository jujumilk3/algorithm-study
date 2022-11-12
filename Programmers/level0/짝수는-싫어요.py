def solution(n):
    return [x for x in range(n + 1) if x % 2 != 0]


assert solution(10) == [1, 3, 5, 7, 9]
assert solution(15) == [1, 3, 5, 7, 9, 11, 13, 15]
