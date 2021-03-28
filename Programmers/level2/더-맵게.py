# def solution(scoville, K):
#     answer = 0
#     scoville.sort(reverse=True)
#     while min(scoville) < K:
#         first = scoville.pop()
#         second = scoville.pop()
#         new = first + (second * 2)
#         scoville.append(new)
#         scoville.sort(reverse=True)
#         answer += 1
#         print(scoville, first, second, new)
#     return answer
"""
첫번째 시도. 런타임 에러 + 효율성 테스트에서 시간초과. 분류가 힙인 것으로 보아 이 문제는 최소힙을 써야한다는 결론.
"""

from heapq import heappop, heappush, heapify


def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while scoville[0] < K and 1 < len(scoville):
        first = heappop(scoville)
        second = heappop(scoville)
        new = first + (second * 2)
        heappush(scoville, new)
        answer += 1
    return answer if scoville[0] >= K else -1
"""
다른 lvl2문제와 달리 생각보다 꽤나 간단했던 문제. 처음 만들었던 코드에는 몇몇 테스트케이스에서 런타임 오류(보통 에러)가 떠서
무슨 문제가 있을까 여러 케이스들을 테스트해봤는데 아니나 다를까 heappop하는 과정에서 다음 원소가 없을 때 (원소가 하나밖에 안남았을 때)
second에서 불러올 요소가 없어서 깨져버리는 것이었다. 그것만 while 조건문에 하나 추가해줘서 간단하게 해결했다. 알고리즘 문제가 요즘
진짜 안풀려서 우울했는데 쉬우면서 자신감을 심어주는 문제였다.
만약에 힙에 대해서 모른다면 https://www.fun-coding.org/Chapter11-heap.html 이곳을 참고해보는 걸 추천한다.
최솟값과 최대값을 찾는 데 보통의 list라면 O(n)의 시간복잡도를 갖고 있지만 heap을 사용하면 파이썬의 경우 O(1)의 시간복잡도를 갖는다.
"""


print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 3, 10, 9, 2, 4], 7))
print(solution([1, 1, 1, 1], 0))
print(solution([0, 0, 0, 0], 3))
