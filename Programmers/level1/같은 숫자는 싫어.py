def solution(arr):
    answer = []
    for i in range(len(arr)):
        if answer and i > 0:
            print(i)
        else:
            answer.append(i)

    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))
