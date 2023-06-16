def solution(strArr):
    zero_list = [0] * 31
    for str in strArr:
        zero_list[len(str)] += 1
    return max(zero_list)
