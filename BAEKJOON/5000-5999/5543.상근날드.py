prices = [int(input()) for _ in range(5)]
print(min(prices[0:3]) + min(prices[3:5]) - 50)
