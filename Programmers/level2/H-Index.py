def solution(citations):
    mins = []
    quote = [0] * len(citations)
    for i in range(len(citations)):
        for j in range(len(citations)):
            if citations[i] <= citations[j]:
                quote[i] += 1
    for i, j in zip(citations, quote):
        mins.append(min(i, j))
    return max(mins)
"""
처음에 문제를 읽었을 땐 설명이 너무 간단하고 입출력 예도 하나밖에 없어서 이게 웬 궤변인가 싶었는데
예제를 하나하나 만들어서 인간의 언어와 뇌로 값들을 도출해보니 생각보다 간단한 문제였다.
쉽게 설명하자면 이렇다.
1편 이상 인용된 논문만 200편이어도 h-index는 1이다.
2편 이상 인용된 논문만 200편이어도 h-index는 2이다.
3편 이상 인용된 논문이 2편 있으면 h-index는 3이 아니다.

그러니까 결국 이거다.
주어진 배열에서 특정 수 A가 나왔을 때 그 숫자와 같거나 큰 숫자들의 갯수를 센다.
A와 같거나 큰 숫자들이 A갯수 이상일 때 A에 대한 h-index 후보는 A가 된다.
만약 주어진 배열에서 A와 같거나 큰 숫자들 A갯수 미만일 때는 A는 후보에 들지 못한다.
난 코드에서 이 숫자를 quote(인용)라는 이름의 list로 정의했다.

예제로 주어진 3, 0, 6, 1, 5에 대해서 이를 정의해보자.
3번 이상 인용된 논문은 3, 6, 5 총 3개이므로 3번 인용된 논문에 대한 h-index 후보는 3이 된다.
마찬가지로 0번 이상은 5개이므로 h-index 후보는 0,
6번 이상은 1개이므로 0,
1번 이상은 4개이므로 1,
5번 이상은 2개이므로 0,

그렇게 각 논문에 대한 h-index후보들 중 가장 큰 요소를 반환해주면 된다.
"""


print(solution([3, 0, 6, 1, 5]))
print(solution([0, 1, 3, 5, 6]))
print(solution([0, 0, 1, 2, 2]))
print(solution([3, 3, 3, 3, 3, 3]))
