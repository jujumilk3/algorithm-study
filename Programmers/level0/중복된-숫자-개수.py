def solution(array, n):
    return array.count(n)


assert solution([1, 1, 2, 3, 4, 5], 1) == 2
assert solution([0, 2, 3, 4], 1) == 0
