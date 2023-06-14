def solution(numbers):
    return eval("*".join(map(str, sorted(numbers, reverse=True)[:2])))
