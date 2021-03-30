def solution(n):
    answer = 0
    for i in range(1, n+1):
        temp_j = 0
        for j in range(i, n+1):
            temp_j += j
            if temp_j == n:
                answer += 1
                break
            elif temp_j > n:
                break
    return answer


print(solution(15))

