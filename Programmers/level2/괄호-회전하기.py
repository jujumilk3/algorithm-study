def solution(s):
    answer = 0
    for i in range(len(s)):
        if i > 0:
            s = s[1:len(s) + 1] + s[0]
        right = True
        big = []
        middle = []
        small = []
        for p in s:
            if p == '(':
                small.append(p)
            elif p == '{':
                middle.append(p)
            elif p == '[':
                big.append(p)
            elif p == ')' and '(' in small:
                del small[small.index('(')]
            elif p == '}' and '{' in middle:
                del middle[middle.index('{')]
            elif p == ']' and '[' in big:
                del big[big.index('[')]
            elif p == ')' and '(' not in small:
                right = False
                break
            elif p == '}' and '{' not in middle:
                right = False
                break
            elif p == ']' and '[' not in big:
                right = False
                break
        if len(big) > 0 or len(middle) > 0 or len(small) > 0:
            right = False
        if right:
            answer += 1
    return answer


print(solution('[](){}'))
print(solution('}]()[{'))
print(solution('[)(]'))
print(solution('}}}'))
print(solution('([{)}]'))
