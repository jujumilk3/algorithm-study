def solution(numbers):
    answer_set = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer_set.add(numbers[i] + numbers[j])
    answer = list(answer_set)
    answer.sort()
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
