case_count = int(input())

for i in range(1, case_count + 1):
    depth = int(input())
    pascal = []
    for j in range(depth):
        row = []
        for k in range(j+1):
            number = 1
            if 1 < j != k and k != 0:
                number = pascal[j-1][k-1] + pascal[j-1][k]
            row.append(number)
        pascal.append(row)
    print('#{}'.format(i))
    for row in pascal:
        print(*row)
