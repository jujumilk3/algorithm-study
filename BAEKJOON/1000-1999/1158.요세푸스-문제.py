N, K = map(int, input().split())
numbers = list(range(1, N+1))
result = []
idx = 0
count = N
K -= 1
while count:
    idx = (idx+K) % count
    result.append(numbers.pop(idx))
    count -= 1
print('<' + ', '.join(list(map(str, result))) + '>')
