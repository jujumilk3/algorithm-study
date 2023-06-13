def solution(code):
    answer = ""
    mode = False
    for i, char in enumerate(code):
        if char == "1":
            mode = not mode
        else:
            if not mode and i % 2 == 0:
                answer += char
            elif mode and i % 2 != 0:
                answer += char
    return answer if answer else "EMPTY"
