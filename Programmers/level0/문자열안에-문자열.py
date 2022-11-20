def solution(str1, str2):
    return 1 if str2 in str1 else 2


assert solution("ab6CDE443fgh22iJKlmn1o", "6CD") == 1
assert solution("ppprrrogrammers", "pppp") == 2
