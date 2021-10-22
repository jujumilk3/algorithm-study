coordinates = [list(map(int, input().split())) for _ in range(3)]
xs = []
ys = []
for coordinate in coordinates:
    if coordinate[0] not in xs:
        xs.append(coordinate[0])
    else:
        xs.remove(coordinate[0])
    if coordinate[1] not in ys:
        ys.append(coordinate[1])
    else:
        ys.remove(coordinate[1])
print(*xs, *ys)
