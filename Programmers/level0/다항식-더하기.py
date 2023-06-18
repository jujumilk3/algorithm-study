def solution(polynomial):
    xnum = 0
    const = 0
    for c in polynomial.split(" + "):
        if c.isdigit():
            const += int(c)
        else:
            xnum = xnum + 1 if c == "x" else xnum + int(c[:-1])
    if xnum == 0:
        return str(const)
    elif xnum == 1:
        return "x + " + str(const) if const != 0 else "x"
    else:
        return f"{xnum}x + {const}" if const != 0 else f"{xnum}x"
