def f(n):
    if n <= 0:
        return 0
    if n <= 3:
        return n
    print('n=', n)
    a = f(n-2)
    b = f(n-3)
    print(a)
    print(b)
    print()
    return a + b


print(f(8))
