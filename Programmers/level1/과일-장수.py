def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    boxes = [score[x : x + m] for x in range(0, len(score), m)]
    for box in boxes:
        if len(box) == m:
            answer += m * min(box)
    return answer
