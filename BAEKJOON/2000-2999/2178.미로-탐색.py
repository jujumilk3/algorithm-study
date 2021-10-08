col, row = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(col)]
move = [[0] * row for _ in range(col)]
step = [(0, 0)]
move[0][0] = 1

while True:
    x, y = step.pop(0)
    if y == col - 1 and x == row - 1:
        print(move[y][x])
        break

    # right
    if x + 1 < row and move[y][x+1] == 0 and matrix[y][x+1]:
        move[y][x+1] = move[y][x] + 1
        step.append((x+1, y))
    # down
    if y + 1 < col and move[y+1][x] == 0 and matrix[y+1][x]:
        move[y+1][x] = move[y][x] + 1
        step.append((x, y+1))
    # left
    if 0 <= x - 1 and move[y][x-1] == 0 and matrix[y][x-1]:
        move[y][x-1] = move[y][x] + 1
        step.append((x-1, y))
    # up
    if 0 <= y - 1 and move[y-1][x] == 0 and matrix[y-1][x]:
        move[y-1][x] = move[y][x] + 1
        step.append((x, y-1))
