while True:
    a, b, c = map(int, input().split())
    if sum([a, b, c]) == 0:
        exit(0)
    else:
        length = sorted([a, b, c])
        print('right' if length[0]**2 + length[1]**2 == length[2]**2 else 'wrong')
