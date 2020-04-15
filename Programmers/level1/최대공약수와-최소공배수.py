def solution(n, m):
    lcm = n * m
    mod = n % m
    while mod > 0:
        n = m
        m = mod
        mod = n % m
    gcd = m
    lcm = lcm // gcd
    return [gcd, lcm]


print(solution(3, 12))
print(solution(2, 5))
