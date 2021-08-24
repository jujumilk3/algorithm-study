array = []

for i in range(5):
    x = int(input())
    if x < 40:
        x = 40
    array.append(x)

print(int(sum(array)/len(array)))
