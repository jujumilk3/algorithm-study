def solution(s):
    return s[(len(s)-1)//2: (len(s)//2) + 1]


print(solution("abcde"))
print(solution("qwer"))
