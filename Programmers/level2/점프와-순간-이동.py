def solution(N):
    answer = 0
    while N > 0:
        answer += N % 2
        N //= 2
    return answer


def solution(N):
    return bin(N).count("1")
