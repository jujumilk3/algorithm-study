height = int(input())
numbers = [list(map(int, input().split())) for _ in range(height)]
sums = [[0]]

for i in range(1, height):
    for j in range(len(numbers[i])):
        if j == 0:
            numbers[i][j] += numbers[i-1][j]
        elif j == len(numbers[i]) - 1:
            numbers[i][j] += numbers[i-1][j-1]
        else:
            numbers[i][j] += max(numbers[i-1][j-1], numbers[i-1][j])

print(max(numbers[height-1]))
