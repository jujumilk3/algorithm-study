def solution(arr):
    max_len = max(len(arr), len(arr[0]))
    for ar in arr:
        if len(ar) < max_len:
            for i in range(max_len - len(ar)):
                ar.append(0)
    if len(arr) < max_len:
        for i in range(max_len - len(arr)):
            arr.append([0] * max_len)
    return arr
