methods = [1, 3, 5]
n = int(input())
while len(methods) < n:
    methods.append(methods[len(methods)-1] + 2 * methods[len(methods) - 2])
print(methods[n-1] % 10007)
