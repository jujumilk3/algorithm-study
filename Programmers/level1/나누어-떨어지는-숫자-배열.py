def solution(arr, divisor):
    array = [x for x in arr if x % divisor == 0]
    array.sort()
    return array if len(array) else [-1]


print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))
