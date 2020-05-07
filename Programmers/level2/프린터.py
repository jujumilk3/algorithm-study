def solution(priorities, location):
    priority_dict = {}
    answer = 0
    arranged = False

    for k, v in enumerate(priorities):
        priority_dict[k] = v
    print(priority_dict)

    current_priority = 0
    current_index = 0
    while not arranged:
        for i in range(len(priority_dict)):
            if i == 0:
                current_priority = priority_dict[0]
                current_index = 0
            elif current_priority < priority_dict[i]:
                current_priority = priority_dict[i]
                current_index = priority_dict

        if True:
            arranged = True

    return answer


print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 0))
