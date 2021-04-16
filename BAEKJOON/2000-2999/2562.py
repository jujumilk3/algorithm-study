number_list = []
for i in range(9):
    number_list.append(int(input()))
max_num = max(number_list)
print(max_num)
print(number_list.index(max_num) + 1)
