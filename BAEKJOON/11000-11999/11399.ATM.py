n = int(input())
t = list(map(int, input().split()))
t.sort()
result = 0

for i in range(n):
    result += t[i] * (n-i)

print(result)

# 돈 빨리 뽑는 사람이 먼저 뽑아야 효율적이니까.
