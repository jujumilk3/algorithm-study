def solution(ineq, eq, n, m):
    eq = eq.replace("!", "")
    return int(eval(f"{n} {ineq}{eq} {m}"))
