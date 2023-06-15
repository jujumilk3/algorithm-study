def solution(arr, n):
    result = []
    if len(arr) % 2 != 0:
        for i, num in enumerate(arr):
            if i % 2 == 0:
                result.append(num + n)
            else:
                result.append(num)
    else:
        for i, num in enumerate(arr):
            if i % 2 != 0:
                result.append(num + n)
            else:
                result.append(num)

    return result
