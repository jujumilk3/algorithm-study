test_case_count = int(input())
user_input_list = []

integer_list = [1, 2, 4]
for i in range(4, 11):
    integer_list.append(sum(integer_list[-3:]))

for i in range(test_case_count):
    user_input_list.append(int(input()))

for i in range(test_case_count):
    print(integer_list[user_input_list[i] - 1])
