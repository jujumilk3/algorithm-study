def solution(my_strings, parts):
    return "".join([string[x : y + 1] for string, (x, y) in zip(my_strings, parts)])
