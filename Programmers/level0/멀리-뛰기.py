def solution(n):
    if n < 3:
        return n
    combs = [0] * (n + 1)
    combs[1], combs[2] = 1, 2
    for i in range(3, n + 1):
        combs[i] = combs[i - 1] + combs[i - 2]
    return combs[n] % 1234567
