def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)  # 빌려줄 수 있는 애들
    set_lost = set(lost) - set(reserve)  # 빌려야 하는 애들
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n - len(set_lost)


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
