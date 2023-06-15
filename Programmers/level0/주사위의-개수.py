def solution(box, n):
    box = [(x // n) * n for x in box]
    return eval("*".join(list(map(str, box)))) // n**3
