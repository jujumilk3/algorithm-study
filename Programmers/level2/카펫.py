def solution(brown, yellow):
    total_count = brown + yellow
    for column in range(2, total_count + 1):
        if (total_count / column) % 1 == 0:  # 사각형이 만들어지는 조건
            row = total_count // column
            if row >= column and (2 * row) + (2 * column) == brown + 4:  # 네개의 작대기를 겹치면 4개의 겹치는 사각형이 발생하니 그 숫자를 뺌.
                return [row, column]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
