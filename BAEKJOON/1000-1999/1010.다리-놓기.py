from math import factorial

testcase_count = int(input())
bridge_spots = [list(map(int, input().split())) for _ in range(testcase_count)]
for spot in bridge_spots:
    result = factorial(spot[1]) / (factorial(spot[0]) * factorial(spot[1] - spot[0]))
    print(int(result))
