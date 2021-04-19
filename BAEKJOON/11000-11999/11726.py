x = int(input())
if x <= 3:
    print(x)
else:
    count_list = [0, 1, 2]
    for i in range(3, x+1):
        count_list.append(count_list[i - 2] + count_list[i - 1])
    print(count_list[x] % 10007)
