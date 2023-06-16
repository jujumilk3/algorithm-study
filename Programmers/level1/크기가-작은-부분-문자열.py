def solution(t, p):
    numbers = []
    for i in range(len(t) - len(p) + 1):
        if t[i : i + len(p)] <= p:
            numbers.append(t[i : i + len(p)])
    return len(numbers)
