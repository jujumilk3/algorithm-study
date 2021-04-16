x = int(input())
y = str(input())

for i in range(len(y)-1, -1, -1):
    print(int(y[i]) * x)
print(x * int(y))
