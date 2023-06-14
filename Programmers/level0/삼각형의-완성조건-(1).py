def solution(sides):
    max_len = max(sides)
    sides.pop(sides.index(max_len))
    return 1 if sum(sides) > max_len else 2
