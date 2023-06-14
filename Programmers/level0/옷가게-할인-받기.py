price_discount_mapper = {
    500000: 0.80,
    300000: 0.90,
    100000: 0.95,
    0: 1,
}


def solution(price):
    answer = 0
    for k, v in price_discount_mapper.items():
        if price >= k:
            answer = price * v
            break
    return int(answer)
