def solution(arr):
    answer = []
    for num in arr:
        answer = answer + ([num] * num)
    return answer
