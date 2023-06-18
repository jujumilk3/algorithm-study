from collections import Counter


def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine)
    new_list = sorted(list(count.items()), key=lambda x: x[1], reverse=True)

    for i in new_list:
        k -= i[1]
        answer += 1

        if k <= 0:
            break

    return answer
