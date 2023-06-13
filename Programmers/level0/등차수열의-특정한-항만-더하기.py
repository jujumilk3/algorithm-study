def solution(a, d, included):
    return sum([x * included[i] for i, x in enumerate(range(a, (a + len(included) * d), d))])


def solution(a, d, included):
    return sum([x for i, x in enumerate(range(a, (a + len(included) * d), d)) if included[i]])
