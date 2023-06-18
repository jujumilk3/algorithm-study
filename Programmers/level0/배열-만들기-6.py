def solution(arr):
    answer = []
    i = 0
    while i <= len(arr) - 1:
        if not answer:
            answer.append(arr[i])
            i += 1
        elif answer and answer[-1] == arr[i]:
            answer.pop(-1)
            i += 1
        elif answer and answer[-1] != arr[i]:
            answer.append(arr[i])
            i += 1
    return answer or [-1]
