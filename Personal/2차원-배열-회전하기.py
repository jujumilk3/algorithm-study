def solution(matrix):
    N = len(matrix)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = matrix[r][c]
    return ret


print(solution([[1,2,3], [4,5,6], [7,8,9]]))
