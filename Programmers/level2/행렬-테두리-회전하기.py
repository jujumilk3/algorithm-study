def solution(rows, columns, queries):
    matrix = [[0 for _ in range(rows)] for _ in range(columns)]
    answer = []
    number = 1
    for col in range(columns):
        for row in range(rows):
            matrix[col][row] = number
            number += 1
    print(matrix)
    for x1, y1, x2, y2 in queries:
        tmp = matrix[x1-1][y1-1]
        mini = tmp

        # →
        for k in range(x1-1, x2-1):
            test = matrix[k+1][y1-1]
            matrix[k][y1-1] = test
            mini = min(mini, test)

        # ↓
        for k in range(y1-1, y2-1):
            test = matrix[x2-1][k+1]
            matrix[x2-1][k] = test
            mini = min(mini, test)

        # ←
        for k in range(x2-1, x1-1,-1):
            test = matrix[k-1][y2-1]
            matrix[k][y2-1] = test
            mini = min(mini, test)

        # ↑
        for k in range(y2-1, y1-1,-1):
            test = matrix[x1-1][k-1]
            matrix[x1-1][k] = test
            mini = min(mini, test)

        matrix[x1-1][y1] = tmp
        answer.append(mini)

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
print(solution(100, 97, [[1, 1, 100, 97]]))
