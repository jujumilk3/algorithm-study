from itertools import combinations


def solution(relation):
    row_size = len(relation)
    column_size = len(relation[0])
    candidates = []
    combs = []

    for i in range(1, column_size + 1):
        combs.extend(combinations(range(column_size), i))

    for comb in combs:
        combined_row = set([tuple([row[index] for index in comb]) for row in relation])
        if len(combined_row) == row_size:
            candidate = True

            for already in candidates:
                if set(already).issubset(set(comb)):
                    candidate = False
                    break

            if candidate:
                candidates.append(comb)
    return len(candidates)


print(solution([['100', 'ryan', 'music', '2'],
                ['200', 'apeach', 'math', '2'],
                ['300', 'tube', 'computer', '3'],
                ['400', 'con', 'computer', '4'],
                ['500', 'muzi', 'music', '3'],
                ['600', 'apeach', 'music', '2']]))
