def solution(priorities, location):
    answer = 0
    max_priority = max(priorities)
    while True:
        current_priority = priorities.pop(0)
        if max_priority == current_priority:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            max_priority = max(priorities)
        else:
            priorities.append(current_priority)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([1, 2, 3, 2], 2))

