def solution(num):
    answer = ""
    while num:
        num, nam = divmod(num, 3)
        answer = '412'[nam] + answer
        if not nam:
            num -= 1
    return answer


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))
print(solution(10))
print(solution(11))
