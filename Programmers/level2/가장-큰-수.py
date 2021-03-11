# from itertools import permutations
#
#
# def solution(numbers):
#     max_number = 0
#     for perm in list(permutations(numbers)):
#         number = int("".join(map(str, perm)))
#         if max_number < number:
#             max_number = number
#     return str(max_number)

"""
1차시도. itertools패키지의 permutations(순열)함수 사용으로 모든 경우의수로 조합해서 max값을 뽑아 반환 -> 시간초과
"""


def solution(numbers):
    return str(int(''.join(sorted(list(map(str, numbers)), key=lambda x: x*3, reverse=True))))


"""
2차시도. reverse까지는 갔지만 30과 3의 처리. 3이 앞에 와야 더 큰 수가 됨.
인덱스0의 숫자가 같으면 뒤를 조사하는 식으로 해야되나 하면서 다른 방법 찾아봄.
그러다가 아래 방법처럼 주어진 문자열을 3번 곱한 방법을 찾아냈는데 정말 기발하다... ㅜㅜ
위 두번째 케이스를 예로 들면 일반적인 로직으로는 30이 3보다 커서 앞에와서 문제가 되지만
*3을 하면 303030과 333의 비교가 되는데 알고리즘의 조건은 1000이하이므로 한자리수가 오더라도
그 수를 세자리수를 만든 숫자를 다른 숫자들과 비교할 수 있게 되는 것.
예: 90, 9가 있으면 9가 앞에 와야 큰 숫자를 만들 수 있는데 이것을
그냥 정렬해버리면 90,9가 되므로 가장 큰 값을 만들 수 없다.
문자열의 정렬은 각 자리에 들어있는 글자의 ASCII값을 기준으로 정렬되므로.
*3을 해서 909090과 999를 비교하면 두번째 글자에서 0(ASCII:48)과 9(ASCII:57)를 비교하여 두번째 숫자가
9인 아이를 앞으로 이동. 해결법에 감동...
"""

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
