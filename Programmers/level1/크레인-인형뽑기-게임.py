def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1]:
                bucket.append(board[i][move - 1])
                board[i][move - 1] = 0
                if len(bucket) > 1 and bucket[-1] == bucket[-2]:
                    answer = answer + 2
                    del bucket[-2:]
                break
    return answer


board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]
print(solution(board, [1, 5, 3, 5, 1, 2, 1, 4]))
