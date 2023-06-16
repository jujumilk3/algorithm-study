def solution(arr):
    for i in range(11):
        if len(arr) < 2**i:
            arr = arr + [0] * (2**i - len(arr))
            break
        elif len(arr) == 2**i:
            break
    return arr
