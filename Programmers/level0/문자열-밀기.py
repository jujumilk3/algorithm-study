def solution(A, B):
    answer = 0
    for i in range(len(A)):
        A = A[-1] + A[:-1]
        answer += 1
        if A == B:
            return answer
    return -1


assert solution("hello", "ohell") == 1
assert solution("hello", "lohel") == 2
assert solution("apple", "elppa") == -1
