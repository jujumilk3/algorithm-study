dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def bfs(place, y, x):
    visited = [[0 for x in range(5)] for y in range(5)]
    dq = [[y, x, 0]]
    visited[y][x] = 1
    while dq:
        now = dq.pop(0)
        if 2 >= now[2] >= 1 and place[now[0]][now[1]] == "P":
            return False
        if now[2] > 2:
            break
        for d in range(4):
            y = now[0] + dy[d]
            x = now[1] + dx[d]
            distance = now[2] + 1
            if 0 <= x < 5 and 0 <= y < 5:
                if place[y][x] != "X" and visited[y][x] == 0:
                    dq.append([y, x, distance])
                    visited[y][x] = 1
    return True


def solution(places):
    answer = []
    for place in places:
        room_is_ok = True
        for y in range(5):
            for x in range(5):
                if place[y][x] == "P":
                    if not bfs(place, y, x):
                        room_is_ok = False
                        break
            if not room_is_ok:
                break
        if not room_is_ok:
            answer.append(0)
        else:
            answer.append(1)
    return answer


print(solution([['POOOP',
                 'OOXOX',
                 'OPXPX',
                 'OOXOX',
                 'POXXP'],

                ['POOPX',
                 'OXPXP',
                 'PXXXO',
                 'OXXXO',
                 'OOOPP'],

                ['PXOPX',
                 'OXOXP',
                 'OXPOX',
                 'OXXOP',
                 'PXPOX'],

                ['OOOXX',
                 'XOOOX',
                 'OOOXX',
                 'OXOOX',
                 'OOOOO'],

                ['PXPXP',
                 'XPXPX',
                 'PXPXP',
                 'XPXPX',
                 'PXPXP']]))


"""
BFS를 하는데 큐에 distance라는 새로운 요소를 넣어서 manhattan distance라는 요소까지 넣어서 계산하는 거임.
if now[2] > 2:
    break
라는 break문을 통해 3번 이상 진행된 step은 짤라내고
"""
