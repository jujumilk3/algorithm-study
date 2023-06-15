def solution(arr, intervals):
    answer = []
    for x, y in intervals:
        answer = answer + arr[x : y + 1]
    return answer
