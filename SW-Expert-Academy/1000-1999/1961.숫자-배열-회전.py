case_count = int(input())

for i in range(1, case_count + 1):
    length = int(input())
    matrix = [list(map(int, input().split())) for _ in range(length)]
    rotate_90 = [[0] * length for _ in range(length)]
    rotate_180 = [[0] * length for _ in range(length)]
    rotate_270 = [[0] * length for _ in range(length)]
    for col in range(length):
        for row in range(length):
            rotate_90[row][length-col-1] = matrix[col][row]
            rotate_180[length-col-1][length-row-1] = matrix[col][row]
            rotate_270[length-row-1][col] = matrix[col][row]

    print('#{}'.format(i))
    for col in range(length):
        print(''.join(list(map(str, rotate_90[col]))), end=' ')
        print(''.join(list(map(str, rotate_180[col]))), end=' ')
        print(''.join(list(map(str, rotate_270[col]))))


"""
2
3
1 2 3
4 5 6
7 8 9
6
6 9 4 7 0 5
8 9 9 2 6 5
6 8 5 4 9 8
2 2 7 7 8 4
7 5 1 9 7 9
8 9 3 9 7 6
"""

"""
10
3
1 2 3
4 5 6
7 8 9
6
6 9 4 7 0 5
8 9 9 2 6 5
6 8 5 4 9 8
2 2 7 7 8 4
7 5 1 9 7 9
8 9 3 9 7 6
7
9 3 1 8 5 0 5
1 1 1 7 9 1 8
3 6 1 4 7 7 4
3 1 8 5 3 0 7
2 5 2 5 7 6 8
2 8 5 2 6 7 0
0 5 5 9 3 6 0
3
6 0 4
7 9 3
8 1 2
6
1 6 4 0 8 1
0 8 0 4 1 2
7 7 6 8 4 3
8 6 3 8 0 0
5 7 7 7 6 4
9 1 8 1 7 1
3
4 1 9
9 9 7
8 0 1
5
1 0 2 2 7
5 2 4 8 5
4 7 8 2 3
9 6 2 8 5
9 6 1 6 6
3
4 8 3
4 6 3
3 9 6
3
4 9 7
0 1 3
4 4 3
5
1 1 7 4 1
0 7 9 3 5
5 2 5 8 6
6 1 9 0 6
7 0 1 3 9
"""
