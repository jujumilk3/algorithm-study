def solution(n, num_list):
    return [x for x in num_list if x % n == 0]


assert solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12]) == [6, 9, 12]
assert solution(5, [1, 9, 3, 10, 13, 5]) == [10, 5]
assert solution(12, [2, 100, 120, 600, 12, 12]) == [120, 600, 12, 12]
