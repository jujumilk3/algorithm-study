def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        if not str(i).replace("5", "").replace("0", ""):
            answer.append(i)
    return answer or [-1]
