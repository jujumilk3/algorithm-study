def solution(a, b, c):
    if len({a, b, c}) == 3:
        return a + b + c
    elif len({a, b, c}) == 1:
        return (a + b + c) * ((a**2) + (b**2) + (c**2)) * ((a**3) + (b**3) + (c**3))
    else:
        return (a + b + c) * ((a**2) + (b**2) + (c**2))
