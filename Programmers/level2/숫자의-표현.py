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
"""
1차시도. 로직은 정답이었으나 시간초과가 떴다. O(n^2)미만의 시간복잡도를 가진 로지
"""


print(solution(15))

