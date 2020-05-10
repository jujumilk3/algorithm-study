def solution(priorities, location):
    priority_dict = {}
    answer = 0
    arranged = False

    for k, v in enumerate(priorities):
        priority_dict[k] = v
    print(priority_dict)

    for i in range(len(priority_dict)):
        print(priority_dict)

    return answer


print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 0))
