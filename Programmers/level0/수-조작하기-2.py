val_mapper = {-1: "w", 1: "s", -10: "d", 10: "a"}


def solution(numLog):
    return "".join([val_mapper[numLog[i - 1] - numLog[i]] for i in range(1, len(numLog))])
