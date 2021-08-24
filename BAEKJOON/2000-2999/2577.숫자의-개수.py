x = int(input())
y = int(input())
z = int(input())

result = str(x * y * z)

for i in range(10):
    print(result.count(str(i)))
