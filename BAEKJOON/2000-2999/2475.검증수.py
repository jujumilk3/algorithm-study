numbers = [x ** 2 for x in list(map(int, input().split()))]
print(sum(numbers) % 10)
