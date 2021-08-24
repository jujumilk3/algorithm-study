def arithmetic_checker(input_number):
    result = False
    number_list = [int(i) for i in [*str(input_number)]]
    if len(number_list) < 3:
        result = True
    else:
        first_common_difference = number_list[1] - number_list[0]
        for i in range(0, len(number_list) - 1):
            common_difference = number_list[i + 1] - number_list[i]
            if first_common_difference != common_difference:
                result = False
                break
            else:
                result = True
    return result


arithmetic_count = 0
input_number = int(input())
for i in range(1, input_number + 1):
    # print(i, " is ", arithmetic_checker(i))
    arithmetic_count += arithmetic_checker(i)

print(arithmetic_count)
