def solution(quiz):
    return ["O" if eval(x) else "X" for x in map(lambda x: x.replace("=", "=="), quiz)]


assert solution(["3 - 4 = -3", "5 + 6 = 11"]) == ["X", "O"]
assert solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]) == ["O", "O", "X", "O"]
