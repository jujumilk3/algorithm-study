def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i < 1 or arr[i-1] != arr[i]:
            answer.append(arr[i])
    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))
