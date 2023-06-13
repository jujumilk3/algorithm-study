def solution(num_list):
    evens = "".join([str(x) for x in num_list if x % 2 == 0])
    odds = "".join([str(x) for x in num_list if x % 2 != 0])
    return int(evens) + int(odds)
