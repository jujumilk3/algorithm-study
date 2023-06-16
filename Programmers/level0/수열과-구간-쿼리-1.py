def solution(arr, queries):
    for i, j in queries:
        for ii in range(i, j + 1):
            arr[ii] += 1
    return arr
