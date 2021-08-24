N, X = list(map(int, input().split()))
numbers = list(map(int, input().split()))
for number in [x for x in numbers if x < X]:
    print(number, end=' ')
