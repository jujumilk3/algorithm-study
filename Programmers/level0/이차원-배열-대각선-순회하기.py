def solution(board, k):
    answer = 0
    length = len(board)
    for i in range(length):
        for j in range(len(board[0])):
            if i + j <= k:
                answer += board[i][j]
    return answer
