numbers_count = int(input())
numbers = []
for _ in range(numbers_count):
    number = int(input())
    if number != 0:
        numbers.append(number)
    else:
        numbers.pop()
print(sum(numbers))
