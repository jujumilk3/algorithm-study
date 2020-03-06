def solution(n):
    return sum(list([x for x in range(1, n + 1) if n % x == 0]))


print(solution(12))
print(solution(5))