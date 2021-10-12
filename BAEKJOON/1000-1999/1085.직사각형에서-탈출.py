x, y, w, h = list(map(int, input().split()))
print(min(0+x, 0+y, w-x, h-y))
