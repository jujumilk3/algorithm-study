def solution(s):
    while len(s) > 1:
        for i in range(len(s)-1):
            check_chars = s[i:i+2]
            if check_chars[0] == check_chars[1]:
                s = s[:i] + s[i+2:]
                break
            elif i == len(s)-2:
                s = 'd'
                break
    return 1 if len(s) == 0 else 0


print(solution("baabaa"))
print(solution("cdcd"))
