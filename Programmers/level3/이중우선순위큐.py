def solution(operations):
    answer = []
    for op in operations:
        com, val = op.split()
        val = int(val)
        if com == "I":
            answer.append(val)
        elif com == "D" and val == 1 and answer:
            answer.pop(answer.index(max(answer)))
        elif com == "D" and val == -1 and answer:
            answer.pop(answer.index(min(answer)))
    return [max(answer), min(answer)] if answer else [0, 0]
