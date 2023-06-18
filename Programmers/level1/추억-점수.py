def solution(name, yearning, photo):
    answer = []
    name_score_dict = {x: y for x, y in zip(name, yearning)}
    print(name_score_dict)
    for ph in photo:
        answer.append(sum([name_score_dict.get(x, 0) for x in ph]))
    return answer
