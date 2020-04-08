def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))


print(solution(118372))