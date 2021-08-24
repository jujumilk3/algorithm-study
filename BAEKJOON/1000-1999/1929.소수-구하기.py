start, end = map(int, input().split())

end += 1
sieves = [True] * end
for i in range(2, int(end ** 0.5) + 1):
    if sieves[i]:
        for j in range(2 * i, end, i):
            sieves[j] = False

for i in range(start, end):
    if i > 1 and sieves[i]:
        print(i)
