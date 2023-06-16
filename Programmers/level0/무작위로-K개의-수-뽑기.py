def solution(arr, k):
    answer = []
    for num in arr:
        if num not in answer:
            answer.append(num)
    return answer + ((k - len(answer[:k])) * [-1]) if len(answer) < k else answer[:k]
