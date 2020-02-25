# https://programmers.co.kr/learn/courses/30/lessons/12912


def solution(a, b):
    small = a if a < b else b
    big = a if a > b else b
    answer = sum(range(small, big+1))
    return answer


print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))
