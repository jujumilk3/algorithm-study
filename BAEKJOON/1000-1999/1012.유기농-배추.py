dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

testcase_count = int(input())

for _ in range(testcase_count):
    row_size, col_size, cabbages_count = map(int, input().split())
    matrix = [[0] * row_size for _ in range(col_size)]
    for __ in range(cabbages_count):
        cabbage_x, cabbage_y = map(int, input().split())
        matrix[cabbage_y][cabbage_x] = 1
    queue = []
    count = 0
    for col in range(col_size):
        for row in range(row_size):
            if matrix[col][row]:
                matrix[col][row] = 0
                count += 1
                queue.append([col, row])
                while queue:
                    y, x = queue.pop(0)
                    for i in range(4):
                        to_x = x+dx[i]
                        to_y = y+dy[i]
                        if 0 <= to_x < row_size and 0 <= to_y < col_size and matrix[to_y][to_x]:
                            matrix[to_y][to_x] = 0
                            queue.append([to_y, to_x])
    print(count)
