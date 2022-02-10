numbers = [1, 1, 1, 2, 2]
case_count = int(input())
input_numbers = [int(input()) for _ in range(case_count)]
while len(numbers) < max(input_numbers):
    numbers.append(numbers[len(numbers)-1] + numbers[len(numbers)-5])
for number in input_numbers:
    print(numbers[number-1])


"""
회고
주소: https://www.acmicpc.net/problem/9461
전전거 + 전전전거인줄 (6번째는 2+1=3) 알았는데 바로전거 + 5번째 전거였음. 
"""
