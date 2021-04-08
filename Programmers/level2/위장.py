from itertools import combinations


def solution(clothes):
    answer = 1
    clothes_dict = {}
    for camo in clothes:
        if not clothes_dict.get(camo[1]):
            clothes_dict[camo[1]] = 1
        else:
            clothes_dict[camo[1]] += 1
    items_list = list(clothes_dict.values())
    for i in range(1, len(items_list) + 1):
        for j in list(combinations(items_list, i)):
            answer += eval('*'.join([str(n) for n in j]))
    return answer
"""
처음에 풀었던 방법. 로직은 맞았으나 1번에서 시간초과가 뜬다. 그래서 다른 사람들의 케이스도 찾아보니까 조금 논란이 있는 문제였다.
그러니까 일종의 "수학적 공식을 대입"해서 풀지 않으면 1번에서 통과가 되지 않게 처리해놓은 구조였다.

난 부위별로 들어온 옷 종류의 갯수를 list에 저장해놓고, 그 종류를 선택하는 조합을 전부 구해서 더하는 방식으로 해결하였다.
순열과 조합에서 필요한 수학공식을 대입해야만 풀 수 있는 문제였다. 수정한 코드가 바로 아래 형태이다.
"""
def solution(clothes):
    answer = 1
    clothes_dict = {}
    for camo in clothes:
        if not clothes_dict.get(camo[1]):
            clothes_dict[camo[1]] = 1
        else:
            clothes_dict[camo[1]] += 1
    items_list = list(clothes_dict.values())
    for v in items_list:
        answer *= v+1
    return answer - 1
"""
내가 combinations함수를 써서 조합을 구해 각 경우의 수를 곱한 부분이 간단하게 해결이 되었다.
특정 순열들에서 각 요소를 뽑는 모든 경우의 수는 순열의 길이 * 순열의 길이 * 순열의 길이--- 가 되는데
거기에 있어서 각 순열에서 아무것도 선택하지 않는 경우의 수를 위해 v+1의 +1이 들어가고,
이 문제에 있어서 모두 벗은 경우는 제외하므로 마지막의 answer에 - 1 이 붙는다.
처음에는 로직은 맞는데 시간초과때문에 틀려서 좀 짜증이 났었는데 4000ms까지 걸렸던 로직이 0.01ms안에 전부 처리가 되는 거 보니
역시 공부하고 배워야겠다는 생각이 절로 들었다.
"""


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"], ["green_turban", "headgear"], ["black_turban", "headgear"], ["bluesunglasses", "eyewear"]]))
