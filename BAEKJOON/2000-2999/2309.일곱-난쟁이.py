from itertools import combinations
heights = [int(input()) for _ in range(9)]
combs = list(combinations(heights, 7))
for comb in combs:
    if sum(comb) == 100:
        for height in sorted(comb):
            print(height)
        break
