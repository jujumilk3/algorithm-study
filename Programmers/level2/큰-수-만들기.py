from itertools import combinations


def solution(number, k):
    perms = list(combinations(number, len(number) - k))
    numbers = []
    for perm in perms:
        numbers.append(''.join(perm))
    return max(numbers)


"""
1차시도. 조합을 이용해서 최대수를 리턴하는 방법을 사용함. 로직은 맞지만 시간초과.
combinations함수가 O(n!)의 시간복잡도를 갖고 있기 때문인 것 같다.
"""


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
