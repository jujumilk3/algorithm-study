from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def solution(maps):
    col_len = len(maps)
    row_len = len(maps[0])

    passed = [[-1 for _ in range(row_len)] for _ in range(col_len)]
    passed[0][0] = 1

    queue = deque()
    queue.append([0, 0])

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            to_x = x + dx[i]
            to_y = y + dy[i]

            if 0 <= to_y < col_len and 0 <= to_x < row_len and maps[to_y][to_x] == 1:
                if passed[to_y][to_x] == -1:
                    passed[to_y][to_x] = passed[y][x] + 1
                    queue.append([to_y, to_x])

        # for row in passed:
        #     print(row)
        # print("====================")
    return passed[-1][-1]


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
