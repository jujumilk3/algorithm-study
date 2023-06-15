import itertools


def solution(number):
    answer = 0
    combs = list(itertools.combinations(number, 3))
    for comb in combs:
        if sum(comb) == 0:
            answer += 1
    return answer
