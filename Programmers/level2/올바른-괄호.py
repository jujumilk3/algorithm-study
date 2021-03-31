def solution(s):
    answer = True
    counter = 0
    for p in s:
        if p == ')':
            counter -= 1
        else:
            counter += 1
        if counter < 0:
            answer = False
            break
    if counter > 0:
        answer = False
    return answer


print(solution("()()"))
print(solution("(())()"	))
print(solution(")()("))
print(solution("(()("))
