count = int(input())
result_list = []
for i in range(count):
    number_input = input().split()
    number_input = map(int, number_input)
    result_list.append(sum(number_input))

for number in result_list:
    print(number)
