def solution(A, B):
    answer = 0
    for i in range(len(A)):
        if A == B:
            return answer
        A = A[-1] + A[:-1]
        answer += 1
    return -1


def solution2(A, B):
    AA = A + A
    answer = AA.find(B)
    if answer > 0:
        answer = len(A) - answer
    return answer


assert solution("hello", "ohell") == 1
assert solution("hello", "lohel") == 2
assert solution("apple", "elppa") == -1
assert solution2("hello", "ohell") == 1
assert solution2("hello", "lohel") == 2
assert solution2("apple", "elppa") == -1