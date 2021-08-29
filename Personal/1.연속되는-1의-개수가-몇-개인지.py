def solution(array):
    answer = []
    straight = 0
    for index, blank in enumerate(array):
        if blank:
            straight += 1
        else:
            if straight:
                answer.append(straight)
            straight = 0
        if index == len(array) - 1 and blank:
            answer.append(straight)
    return answer


print(solution([1, 1, 1, 0, 1]))
print(solution([0, 0, 0, 1, 0]))
print(solution([0, 1, 0, 1, 1]))
print(solution([1, 1, 1, 1, 1]))
print(solution([0, 0, 1, 1, 1]))
print(solution([1, 1, 1, 0, 1, 1, 1]))
