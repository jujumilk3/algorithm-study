def solution(chicken):
    answer = 0
    idx = 0
    while chicken:
        idx += 1
        chicken -= 1
        if idx % 10 == 0:
            chicken += 1
            answer += 1
    return answer


def solution(chicken):
    return int(chicken * 0.11111111111)
