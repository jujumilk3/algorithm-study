from itertools import combinations


def solution(orders, course):
    order_dict = {}
    length_max = [0] * max(course)
    arranged_orders = []
    for order in orders:
        arranged_orders.append(sorted(order))
    for order in arranged_orders:
        for food_count in course:
            for comb in list(combinations(order, food_count)):
                current_course = ''.join(comb)
                if current_course in order_dict:
                    order_dict[current_course] += 1
                else:
                    order_dict[current_course] = 1
                if length_max[len(current_course)-1] < order_dict[current_course]:
                    length_max[len(current_course)-1] = order_dict[current_course]
    result = {k: v for k, v in order_dict.items() if v == length_max[len(k)-1] and v > 1}
    return sorted(list(result.keys()))
"""
코드의 흐름은 이렇다. 먼저 들어온 주문을 알파벳 오름차순으로 정렬한다. 그다음 그 배열을 가지고
만들 수 있는 조합(combinations)을 모두 만든 다음에 해당 조합이 나온 숫자만큼 dict에 count를 해준다.
그리고 동시에 length_max에 각 코스의 길이만큼 제일 많이 나온 코스의 갯수를 갱신해준다.
예를 들어 첫번째 예제에서는 AC가 네 번, CDE가 3번, BCFG와 ACDE가 두번씩 나왔으므로
length_max의 모양은 [0, 4, 3, 2]가 되는 것이다.
여기까지 구했으면 결과값으로 모든 코스를 조사해가면서 그 코스가 1회 이상 나왔는지, 그리고
같은 코스 길이를 가진 다른 코스들보다 제일 많이 나왔는지 조사해서 넣어준 다음에 그것 또한
알파벳 오름차순 정렬하여 반환하면 된다.

맨 처음에 orders 배열의 원소들을 알파벳 오름차순 처리가 돼있지 않다는 걸 깨닫지 못하고
오답을 냈었는데 3번째 케이스에서 WX가 두 번 들어가있었는데 정렬을 해놓지 않으니 XW와 WX를 다른 코스로
인식하여 제대로 된 답을 도출하고 있지 못했던 것이었다. 그부분만 해결하니 바로 정답처리 돼있다.
아무래도 문제가 길면 길수록 제한사항이나 그런 디테일에 좀 집중하기 힘든 것 같다...
중복문제를 만들지 않기 위한 제작자들의 노고도 이해는 가지만 주기적으로 코드 챌린지에 참여하고 있는데
알고리즘의 난이도는 둘째치고 뭔가 가면 갈수록 문제가 길어지고 이해하기 힘들어진다는 생각이 든다.

플러스로 이건 문제를 풀고 나서 알았는데 파이썬 표준 라이브러리에 collections라는 패키지가 있고
이 안에 Counter라는 함수가 있는데 이것이 원소의 숫자를 세주는 함수였다. 이 함수를 이용하면 좀 더 쉽게 해결할 수 있을 것이다.
"""


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]	))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]	))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]	))
