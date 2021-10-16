coordinates_count = int(input())
coordinates = [list(map(int, input().split())) for _ in range(coordinates_count)]
for x, y in sorted(coordinates, key=lambda x: (x[0], x[1])):
    print(x, y)
