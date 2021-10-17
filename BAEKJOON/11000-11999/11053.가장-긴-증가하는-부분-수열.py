numbers_count = int(input())
numbers = list(map(int, input().split()))
dp = [1 for _ in range(numbers_count)]

for i in range(numbers_count):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
