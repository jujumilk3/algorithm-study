computers_count = int(input())
connections_count = int(input())
matrix = [[0] * (computers_count+1) for _ in range(computers_count+1)]

for _ in range(connections_count):
    connection = list(map(int, input().split()))
    matrix[connection[0]][connection[1]] = 1
    matrix[connection[1]][connection[0]] = 1


def dfs(current_node, row, foot_prints):
    foot_prints += [current_node]
    for search_node in range(len(row[current_node])):
        if row[current_node][search_node] and search_node not in foot_prints:
            foot_prints = dfs(search_node, row, foot_prints)
    return foot_prints


print(len(dfs(1, matrix, []))-1)

