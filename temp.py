from math import gcd

def lcm(m, n):
    return m * n // gcd(m, n)

print(lcm(78696, 19332))
