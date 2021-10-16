def solution(rows, columns, queries):
    matrix = [[row * columns + col + 1 for col in range(columns)] for row in range(rows)]
    answer = []

    for t, l, b, r in queries:
        top, left, bottom, right = t-1, l-1, b-1, r-1
        tmp = matrix[top][left]
        minimum = tmp

        # left
        for y in range(top, bottom):
            value = matrix[y+1][left]
            matrix[y][left] = value
            minimum = min(minimum, value)
        # bottom
        for x in range(left, right):
            value = matrix[bottom][x+1]
            matrix[bottom][x] = value
            minimum = min(minimum, value)
        # right
        for y in range(bottom, top, -1):
            value = matrix[y-1][right]
            matrix[y][right] = value
            minimum = min(minimum, value)
        # top
        for x in range(right, left, -1):
            value = matrix[top][x-1]
            matrix[top][x] = value
            minimum = min(minimum, value)

        matrix[top][left+1] = tmp
        answer.append(minimum)

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
print(solution(100, 97, [[1, 1, 100, 97]]))
