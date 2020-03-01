def solution(s):
    len_correct = len(s) == 4 or len(s) == 6
    return s.isnumeric() and len_correct


# 이하 좋은 풀이
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)


print(solution("a234"))
print(solution("1234"))
