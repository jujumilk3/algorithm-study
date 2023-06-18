def solution(a, b, c, d):
    answer = 0
    origin = [a, b, c, d]
    arr = list(set(origin))

    if len(arr) == 4:
        answer = min(arr)
    elif len(arr) == 3:
        p = max(origin, key=origin.count)
        tmp = [num for num in arr if num != p]
        answer = tmp[0] * tmp[1]
    elif len(arr) == 2:
        if max([origin.count(num) for num in arr]) > 2:
            p = max(origin, key=origin.count)
            q = min(origin, key=origin.count)
            answer = pow(((10 * p) + q), 2)
        else:
            answer = (arr[0] + arr[1]) * abs(arr[0] - arr[1])
    elif len(arr) == 1:
        answer = int(str(arr[0]) * 4)

    return answer
