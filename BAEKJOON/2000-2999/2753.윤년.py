year = int(input())
result = 1 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 0
print(result)