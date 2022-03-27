def solution(s):
    answer = 0
    for i in range(len(s)):
        s = s[1:len(s) + 1] + s[0]
        stack = []
        right = True
        for p in s:
            if p == '(' or p == '{' or p == '[':
                stack.append(p)
            else:
                if len(stack) < 1:
                    right = False
                    break
                current_p = stack.pop()
                if p == ')' and current_p != '(':
                    right = False
                    break
                elif p == '}' and current_p != '{':
                    right = False
                    break
                elif p == ']' and current_p != '[':
                    right = False
                    break
        if right and len(stack) < 1:
            answer += 1
    return answer


print(solution('[](){}'))
print(solution('}]()[{'))
print(solution('[)(]'))
print(solution('}}}'))
print(solution('([{)}]'))
