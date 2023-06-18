def solution(rank, attendance):
    scores = sorted([rank[i] for i, x in enumerate(attendance) if x])
    a, b, c = scores[:3]
    return 10000 * rank.index(a) + 100 * rank.index(b) + rank.index(c)
