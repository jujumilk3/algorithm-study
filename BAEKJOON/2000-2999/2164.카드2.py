N = int(input())
square = 2

while True:
    if N == 1 or N == 2:
        print(N)
        break
    else:
        square *= 2
        if square >= N:
            print((N - (square // 2)) * 2)
            break
