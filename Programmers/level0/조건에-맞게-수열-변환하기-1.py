def solution(arr):
    def op(x):
        if x >= 50 and x % 2 == 0:
            return x // 2
        elif x < 50 and x % 2 != 0:
            return x * 2
        else:
            return x

    return list(map(op, arr))
