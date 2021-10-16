import sys

numbers_count = int(input())
numbers = [0] * 10001
for i in range(numbers_count):
    numbers[int(sys.stdin.readline())] += 1

for number, count in enumerate(numbers):
    for _ in range(count):
        print(number)
