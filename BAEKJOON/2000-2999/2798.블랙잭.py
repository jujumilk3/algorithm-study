from itertools import combinations

card_count, black_jack = list(map(int, input().split()))
numbers = list(map(int, input().split()))
closest = 0
combs = combinations(numbers, 3)

for comb in combs:
    sum_of_cards = sum(comb)
    if closest < sum_of_cards <= black_jack:
        closest = sum_of_cards
    if closest == black_jack:
        break

print(closest)
