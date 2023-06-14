def solution(num_list):
    evens = sum([x for i, x in enumerate(num_list) if i % 2 == 0])
    odds = sum([x for i, x in enumerate(num_list) if i % 2 != 0])
    return max([evens, odds])
