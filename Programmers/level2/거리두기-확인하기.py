def solution(places):
    search_row_max = 4
    search_column_max = 4
    manhattan_distance_standard = 2
    for i in range(len(places)):
        distance_rule = 1
        print('#######다음방######')
        for y in range(len(places[i])):
            for x, char in enumerate(places[i][y]):
                if char == 'P':
                    search_rows = x + manhattan_distance_standard if x < 3 else search_row_max
                    search_columns = y + manhattan_distance_standard if y < 3 else search_column_max
                    print('여기 사람 있어요!', y, x)
                    print('탐색범위는', search_columns, search_rows)
                    # 가로서치
                    print(places[i][y][x+1:search_rows+1])
                    if 'P' in places[i][y][x+1:search_rows+1]:
                        print('범위 안에 사람이 있어요')
                        print('위치는', y, x)
                    print()

        print()
    answer = []
    return answer


print(solution([['POOOP',
                 'OXXOX',
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


# 1. 사람이 앉은 자리 P가 오면 맨해튼거리가 2 이하인곳 모두를 조사한다.
# 2. 만약에 사람이 있으면 그 둘 사이의 공간을 조사해서 모두 파티션으로 막혀있는지 조사한다.
#    여기에서 사이의 공간을 조사하는 데에는 사선이 아닌 대각선에 존재하는 경우 사이파티션1개
#    혹은 2칸 이상 떨어져있어야 한다. 고로 맨해튼거리를 기준으로 특정 사람이 주어졌을 때
#    조사해야할 범위는
#         0
#        000
#       00P00
#        000
#         0
#    와 같다.
# 3. 고로 P가 주워지면 먼저 조사할 범위를 정의하고
# 4. 그 안에 다른 P가 있는지 확인하고
# 5. 다른 P가 있다면 둘 사이에 파티션 X가 존재하는지 확인.
# 6. 있으면 다음사람으로 넘어가고 없으면 0을 리턴한다.
# 7. 윗줄 왼쪽부터 순차적으로 진행한다면 중복검사자리가 생기니 실제 조사하는 범위는
#        P00
#        00
#        0
#    으로 하면 되겠다.
# 8. 만약에 P가 (0, 0)에 존재하고 있다면 조사할 곳은
#    ( P  ), (0, 1), (0, 2)
#    (1, 0), (1, 1),
#    (2, 0)
#    으로서 합이 2 이하인 숫자들의 조합이 된다.
#    그러니까 P의 x, y를 더한 값의 2 이하가 된다.
#    만약에 (2, 2)에 위치해 있다면 조사범위는
#    (2, 2), (2, 3), (2, 4)
#    (3, 2), (3, 3)
#    (4, 2)
#    가 될터이니 말이다.

# 기타: 수학에서는 좌표를 쓸 때 x값을 먼저 쓰는데 컴퓨터에서는 행먼저 인식해야해서 y값 먼저
# 써야하는게 햇갈릴 수 있음. (내가 햇갈림)
# asdawd
