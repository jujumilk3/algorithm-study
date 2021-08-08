def solution(price, money, count):
    sum_of_prices = sum([x * price for x in range(1, count+1)])
    return abs(money - sum_of_prices) if money < sum_of_prices else 0


print(solution(3, 20, 4))
print(solution(3, 20, 1))
