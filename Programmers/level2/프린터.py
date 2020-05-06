def solution(priorities, location):
    priority_dict = {}
    answer = 0
    for k, v in enumerate(priorities):
        priority_dict[k] = v
    for v in priority_dict.items():
        print(v[1])
    print(priority_dict)
    return answer


print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 0))
