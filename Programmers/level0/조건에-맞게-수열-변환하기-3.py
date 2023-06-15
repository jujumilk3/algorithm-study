def solution(arr, k):
    def op(x):
        if k % 2 == 0:
            return x + k
        else:
            return x * k

    return list(map(op, arr))
