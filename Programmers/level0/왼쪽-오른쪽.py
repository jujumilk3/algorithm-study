def solution(str_list):
    for i, char in enumerate(str_list):
        if char == "l":
            return str_list[:i]
        elif char == "r":
            return str_list[i + 1 :]
    return []
