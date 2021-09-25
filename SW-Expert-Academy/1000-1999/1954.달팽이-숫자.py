case_count = int(input())

for i in range(1, case_count + 1):
    number = int(input())
    matrix = [[0] * number for _ in range(number)]
    x, y = -1, 0
    numbers = [number]
    for j in range(number-1, 0, -1):
        numbers.append(j)
        numbers.append(j)
    rotation = 0
    index = 0
    for j in range(1, (number ** 2)+1):
        if numbers[index] and rotation % 4 == 0:
            x += 1
            matrix[y][x] = j
            numbers[index] -= 1

        if numbers[index] and rotation % 4 == 1:
            y += 1
            matrix[y][x] = j
            numbers[index] -= 1

        if numbers[index] and rotation % 4 == 2:
            x -= 1
            matrix[y][x] = j
            numbers[index] -= 1

        if numbers[index] and rotation % 4 == 3:
            y -= 1
            matrix[y][x] = j
            numbers[index] -= 1

        if numbers[index] == 0:
            index += 1
            rotation += 1

    print('#{}'.format(i))
    for row in matrix:
        print(' '.join(map(str, row)))


"""
2    
3   
4             
"""
