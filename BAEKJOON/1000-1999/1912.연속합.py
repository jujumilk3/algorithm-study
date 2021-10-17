numbers_count = int(input())
numbers = list(map(int, input().split()))
dp = [0] * numbers_count
dp[0] = numbers[0]
for i in range(1, numbers_count):
    dp[i] = max(numbers[i], numbers[i] + dp[i-1])
print(max(dp))
