N = int(input())
founds = []
for i in range(N):
    save = i
    for j in str(i):
        i += int(j)
    if i == N:
        founds.append(save)

print(min(founds) if len(founds) else 0)
