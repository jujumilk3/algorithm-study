def solution(a, b):
    test = list(x * y for x, y in zip(a, b))
    print(test)
    return sum(x * y for x, y in zip(a, b))


print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
print(solution([-1, 0, 1], [1, 0, -1]))
