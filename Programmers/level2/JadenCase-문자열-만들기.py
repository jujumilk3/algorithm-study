def solution(s):
    answer = ''
    wording = False
    for char in s:
        if char == ' ':
            answer += char
            wording = False
        elif not wording:
            answer += char.upper()
            wording = True
        elif wording:
            answer += char.lower()
    return answer
"""
간단하게 공백은 그대로 붙이고, 단어가 처음 오면 대문자, 계속되는 중이면 소문자를 붙이는 식으로 코딩하였다.
하지만 다른 사람들의 답을 보니 `s.title()`이나 `s.capitalize()`같은 간단한 함수를 이용해 해결했더라.
역시 아는 게 많으면 고생을 덜하는 것 같다. 참고로 title함수는 문제의 내용 그대로 구현돼있는 함수이고
capitalize는 문자열이 주어졌을 때 맨 앞자리 글자만 대문자로 바꿔주는 함수이다. 
"""


print(solution("3people unFollowed me"))
print(solution("for the last week"))
print(solution("    asd   qwe"))
print(solution("333333 333333 33333333"))
print(solution("a a a aa a a"))
