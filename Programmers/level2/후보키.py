from itertools import combinations, permutations


def solution(relation):
    column = len(relation[0])
    row = len(relation)
    for i in range(1, column+1):
        combs = list(combinations(range(column), i))

    answer = 0
    return answer


print(solution([['100', 'ryan', 'music', '2'],
                ['200', 'apeach', 'math', '2'],
                ['300', 'tube', 'computer', '3'],
                ['400', 'con', 'computer', '4'],
                ['500', 'muzi', 'music', '3'],
                ['600', 'apeach', 'music', '2']]))


# 각 행의 조합을 구한다.
# 그 조합으로 후보키를 찾는다.
# 어떤 조합으로 후보키를 찾으면 그 조합이 들어가있는 다른 조합들을 전부 없앤다.
