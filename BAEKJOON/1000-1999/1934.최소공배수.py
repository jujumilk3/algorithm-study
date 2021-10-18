testcase_number = int(input())


def gcd(m, n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)


for _ in range(testcase_number):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))
