from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

width, height = map(int, input().split())
matrix = []
queue = deque([])
for i in range(height):
    matrix.append(list(map(int, input().split())))
    for j in range(width):
        if matrix[i][j] == 1:
            queue.append([i, j])

while queue:
    x, y = queue.popleft()
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if 0 <= a < height and 0 <= b < width and matrix[a][b] == 0:
            queue.append([a, b])
            matrix[a][b] = matrix[x][y] + 1

result = 0
for row in matrix:
    if 0 in row:
        print(-1)
        exit(0)
    result = max(result, max(row))
print(result-1)
