def solution(A, B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse=True)))


print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))
