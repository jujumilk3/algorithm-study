# from itertools import combinations


# def solution(number, k):
#     perms = list(combinations(number, len(number) - k))
#     numbers = []
#     for perm in perms:
#         numbers.append(''.join(perm))
#     return max(numbers)
"""
1차로 시도한 코드였다. 조합을 이용해서 최대수를 리턴하는 방법을 사용했는데 로직은 맞지만 시간초과 떴다.
combinations함수가 O(n!)의 시간복잡도를 갖고 있기 때문인 것 같다. 문제분류가 탐욕법으로 돼있었으니까
이렇게 푸는 게 맞는 것 같은데 이 combibations를 대체할 O(n!)미만의 시간복잡도를 가진 함수를 구현하는 게
본래의 출제목적인 것 같다.
"""


# def solution(numbers, k):
#     stack = []
#     last_index = 0
#     for (i, number) in enumerate(numbers):
#         stack.append(number)
#         for j in range(len(stack)-1, -1, -1):
#             if stack[j] < number and k:
#                 stack.pop(j)
#                 k -= 1
#                 continue
#             elif k == 0:
#                 last_index = i
#                 break
#     return ''.join(stack) + numbers[last_index+1:]
"""
2차시도. combinations가 시간초과 뜨니까 다른 사람들의 풀이방법을 검색해봤다. 그러니까 보통 stack으로 해결을 했더라.
그래서 stack이라는 힌트만 가지고 풀어보려 했다. 각 숫자가 들어왔을 때마다 저장을 해놓고, 새로운 숫자를 넣어야 할 때마다 저장을 해 놓은 숫자들을
가장 최근에 넣은 숫자부터 조회해서 새로 넣을 수보다 작으면 없애는 작업을 반복하는 방법이다. 10번케이스 시간초과 및 11번, 12번 오답이 뜨더라...
조금 생각해보니까 같은 숫자만이 주어졌을 때, 혹은 남은 숫자들과 넣어야 할 숫자가 전부 같은 숫자일 때 로직이 부숴진다.
아마 11번 12번은 이런 케이스인 것 같다. 어차피 그 문제를 해결해봤자 10번에서 시간초과가 나기 때문에 이 코드느 그냥 폐기처분 했다.
"""


def solution(number, k):
    st = []
    for i in range(len(number)):
        while st and k > 0 and st[-1] < number[i]:
            st.pop()
            k -= 1
        st.append(number[i])
    return ''.join(st[:len(st) - k])
"""
마지막은 그냥 다른 사람의 풀이. 마지막 숫자를 계속해서 지워가는 방법이었다. 내 코드와 차이가 있다면 굳이 맨 앞까지 찾아가는 코드가 아니라
새로이 넣어야 할 숫자가 있을 때 그 숫자와 자리수가 가장 가까운 숫자부터 비교해나간다는 점이다.

알고리즘이 너무 약한 것 같아서 책을 읽고 공부를 하는데 알고리즘 문제해결전략에서도 이런 얘기가 나오더라. stack을 배우고 queue를 배우고 하는 것은 크게
어렵지 않다. 문제해결방법을 배우고 익히는 것이 정말 어렵다고. 아주 통감하는 바였다. 나도 항상 느끼는 것이기 때문이다. 나도 stack 안다. queue 안다.
탐욕법이 뭔지도, 동적계획법이 뭔지도 알고 이진탐색트리, 그래프, DFS, BFS 다 안다. 하지만 적용에 힘이 든다. 이 문제만 해도 처음에 생각했던 부분이
먹히지 않으니 바로 막혔다. 주어진 숫자에서 몇 개를 제거해서 큰 숫자를 만들어보자는 발상 자체는 이해가 되는데 사람의 방법으로 이케이케 저케저케 숫자를
제거하면 가장 큰 수가 되지! 하는 생각은 들어도 내가 이것을 뇌속에서 어떤식으로 생각해서 어떤 결론을 통해서 나오는 결과물인지도 모르겠고 논리적으로
풀어내기도 힘이 든다. 참. 어렵다.
"""


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
