def solution(arr):
    arr.sort()
    arr = list(set(arr))
    answer = True if arr[len(arr) - 1] == len(arr) else False
    return answer


print(solution([4, 1, 3, 2]))
print(solution([4, 1, 3]))
print(solution([1, 2, 3, 3, 5]))
