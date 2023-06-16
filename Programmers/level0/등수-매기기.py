def solution(score):
    sums = [sum(x) for x in score]
    sorted_sums = sorted(sums, reverse=True)
    score_rank_dict = {}
    rank = 1
    for su in sorted_sums:
        if su not in score_rank_dict:
            score_rank_dict[su] = rank
            rank += sums.count(su)
    return [score_rank_dict[x] for x in sums]
