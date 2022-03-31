def solution(col_len, row_len, board):
    answer = ''
    matrix = [list(row) for row in board]
    for row in matrix:
        print(row)

    for col in range(col_len):
        for row in range(row_len):
            print(matrix[col][row])
    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
