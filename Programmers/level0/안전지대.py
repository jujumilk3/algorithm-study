def solution(board):
    count = 0
    row = [-1, 0, 1]
    col = [-1, 0, 1]
    danger_zone = [[0] * len(board) for _ in range(len(board))]
    danger_zone_index = []
    for r in row:
        for c in col:
            danger_zone_index.append((r, c))

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] == 1:
                for x, y in danger_zone_index:
                    try:
                        if i + x < 0 or j + y < 0 or i + x > len(board) or j + y > len(board):
                            continue
                        danger_zone[i + x][j + y] = "x"
                    except:
                        continue
    for i, row in enumerate(danger_zone):
        for j, col in enumerate(row):
            if danger_zone[i][j] != "x":
                count += 1

    return count
