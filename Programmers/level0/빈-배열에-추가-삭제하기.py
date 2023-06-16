def solution(arr, flags):
    answer = []
    for index, flag in enumerate(flags):
        if flag:
            answer = answer + [arr[index]] * (arr[index] * 2)
        else:
            answer = answer[: -1 * arr[index]]
    return answer
