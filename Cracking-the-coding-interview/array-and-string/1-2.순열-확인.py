"""
※ 문제
문자열 두 개가 주어졌을 때 이 둘이 서로 순열관계에 있는지 확인하는 메서드를 작성하라.

※ 할만한 질문.
1.
2.

※ 계획.
긴쪽을 A, 짧은쪽을 B라고 칭했을 때 B의 요소들을 긴쪽에서 하나하나 찾아서 같이 제거하다가
1. B가 다 제거가 되면 순열인 것이고
2. B다 제거가 안되면 순열이 아님

"""


def solution(string_a, string_b):
    if len(string_a) < len(string_b):
        short = string_a
        long = string_b
    else:
        short = string_b
        long = string_a

    short_list = list(short)
    long_list = list(long)

    return True


print(solution("abcdefghi", "fed"))  # 순열
# print(solution("abcdefghi", "fedd"))  # 순열이 아님

