def solution(N, stages):
    user_count = len(stages)
    stage_map = {}
    for i in range(1, N+1):
        stage_map[i] = stages.count(i) / user_count if user_count else 0
        user_count = user_count - stages.count(i)
    return sorted(stage_map, key=lambda x: stage_map[x], reverse=True)


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(5, [1, 1, 1, 1, 1]))
print(solution(5, [5, 5, 5, 6, 6]))
print(solution(4, [4, 4, 4, 4, 4]))
