def solution(s):
    return True if s.lower().count('p') == s.lower().count('y') else False


print(solution("pPoooyY"))
print(solution("Pyy"))
