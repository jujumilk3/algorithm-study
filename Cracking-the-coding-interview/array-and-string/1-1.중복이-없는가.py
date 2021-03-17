"""
※ 문제
문자열이 주어졌을 때 이 문자열에 같은 문자가 중복되어 등장하는지 확인하는 알고리즘을 작성하라.
자료구조를 추가로 사용하지 않고 풀 수 있는 알고리즘 또한 고민하라.

※ 할만한 질문.
1. 소문자와 대문자는 같은 문자로 치나?
2. 문자열에 스페이스가 들어오나?
2-1. 들어온다면 스페이스의 중복도 중복으로 치나?

※ 계획.
2중 반복문으로 각 문자에 위치에서 뒤로 중복되는 것이 있나 검사하고 있으면 False return.
이렇게 하면 다른 자료구조 안쓰고도 해결 가능
"""


def solution(string: str):
    duplicated = False
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                duplicated = True
    return duplicated


print(solution("abcdefghi"))
print(solution("abcdefghia"))
print(solution("a"))
print(solution("aa"))
