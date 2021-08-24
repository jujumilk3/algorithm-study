case_count = int(input())

for i in range(1, case_count + 1):
    item_count = int(input())
    prices = list(map(int, input(). split()))
    current_profit = 0
    ex_price = 0
    for j in range(item_count-1, -1, -1):
        if prices[j] < ex_price:
            current_profit += ex_price - prices[j]
        if ex_price == 0 or ex_price < prices[j]:
            ex_price = prices[j]
    print('#{} {}'.format(i, current_profit))


"""
4
3
10 7 6
3
3 5 9
5
1 1 3 1 2
5
1 0 3 1 2
"""
