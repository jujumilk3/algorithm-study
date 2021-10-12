number_of_house = int(input())
prices = [list(map(int, input().split())) for _ in range(number_of_house)]
for i in range(1, number_of_house):
    prices[i][0] = min(prices[i - 1][1], prices[i - 1][2]) + prices[i][0]
    prices[i][1] = min(prices[i - 1][0], prices[i - 1][2]) + prices[i][1]
    prices[i][2] = min(prices[i - 1][0], prices[i - 1][1]) + prices[i][2]
print(min(prices[number_of_house - 1]))
