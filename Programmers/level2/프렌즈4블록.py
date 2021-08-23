def solution(col, row, board):
    answer = 0
    for y in range(col):
        print(board[y])
        # for x in range(row):
        #     print(board[y][x])
    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
