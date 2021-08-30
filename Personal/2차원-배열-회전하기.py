def rotate90(matrix):
    N = len(matrix)
    ret = [[0] * N for _ in range(N)]
    for row in range(N):
        for column in range(N):
            ret[column][N-1-row] = matrix[row][column]
    return ret


def rotate180(matrix):
    pass


def rotate270(matrix):
    pass


print(rotate90([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
