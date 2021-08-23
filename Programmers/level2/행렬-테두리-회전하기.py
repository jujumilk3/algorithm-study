def solution(rows, columns, queries):
    matrix = []
    answer = []
    number = 1
    for column in range(rows):
        matrix.append([])
        for row in range(columns):
            matrix[column].append(number)
            number += 1
    for cycle in queries:
        total = []
        horizon = matrix[cycle[0]-1][cycle[1]-1:cycle[3]]
        vertical = [matrix[x][cycle[3]-1] for x in range(cycle[0]-1, cycle[2])]
        horizon_oppo = matrix[cycle[2]-1][cycle[1]-1:cycle[3]][::-1]
        vertical_oppo = [matrix[x][cycle[1]-1] for x in range(cycle[0]-1, cycle[2])][::-1]
        total.append(min(horizon))
        total.append(min(vertical))
        total.append(min(horizon_oppo))
        total.append(min(vertical_oppo))
        print(horizon)
        print(vertical)
        print(horizon_oppo)
        print(vertical_oppo)
        print()
        answer.append(min(total))
    print("===================")
    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
print(solution(100, 97, [[1, 1, 100, 97]]))
