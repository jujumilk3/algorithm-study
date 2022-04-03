def gcd(m, n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)


from math import gcd

print(gcd(78696, 19332))
# 36

from math import gcd

def lcm(m, n):
    return m * n // gcd(m, n)

print(lcm(78696, 19332))
# 42259752
