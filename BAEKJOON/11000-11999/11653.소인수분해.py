N = int(input())
div = 2
while N != 1:
    if N % div == 0:
        N //= div
        print(div)
    else:
        div += 1
