def solution(arr):
    if len(arr) > 1 and min(arr):
        del arr[arr.index(min(arr))]
    else:
        arr = [-1]
    return arr


print(solution([4, 3, 2, 1]))
print(solution([10]))
