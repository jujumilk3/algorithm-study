def solution(my_string):
    return eval("+".join(filter(str.isdigit, my_string)))
