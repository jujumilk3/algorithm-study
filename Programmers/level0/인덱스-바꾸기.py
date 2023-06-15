def solution(my_string, num1, num2):
    as_list = list(my_string)
    as_list[num1], as_list[num2] = as_list[num2], as_list[num1]
    return "".join(as_list)
