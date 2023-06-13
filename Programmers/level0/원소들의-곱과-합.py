def solution(num_list):
    multi = 1
    for num in num_list:
        multi *= num
    return int(multi < sum(num_list) ** 2)
