def solution(v):
    answer = []
    first_stack = []
    second_stack = []
    for i in range(len(v)):
        if v[i][0] not in first_stack:
            first_stack.append(v[i][0])
        else:
            first_stack.remove(v[i][0])
        if v[i][1] not in second_stack:
            second_stack.append(v[i][1])
        else:
            second_stack.remove(v[i][1])
    answer.append(*first_stack)
    answer.append(*second_stack)
    return answer


print(solution([[1, 4], [3, 4], [3, 10]]))
print(solution([[1, 1], [2, 2], [1, 2]]))
