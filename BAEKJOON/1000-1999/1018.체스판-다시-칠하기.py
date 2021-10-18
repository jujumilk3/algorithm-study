col, row = map(int, input().split())
matrix = [list(input()) for _ in range(col)]
result = []

for i in range(col-7):
    for j in range(row-7):
        w_start = 0
        b_start = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if matrix[k][l] != 'W':
                        w_start = w_start+1
                    if matrix[k][l] != 'B':
                        b_start = b_start + 1
                else:
                    if matrix[k][l] != 'B':
                        w_start = w_start+1
                    if matrix[k][l] != 'W':
                        b_start = b_start + 1
        result.append(w_start)
        result.append(b_start)

print(min(result))
