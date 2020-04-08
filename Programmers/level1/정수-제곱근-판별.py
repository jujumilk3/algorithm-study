def solution(n):
    return int(((n ** 0.5) + 1)) ** 2 if (n ** 0.5).is_integer() else -1


print(solution(121))
print(solution(3))

