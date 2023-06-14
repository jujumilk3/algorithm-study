def solution(num_list):
    op = "+" if len(num_list) >= 11 else "*"
    return eval(op.join(map(str, num_list)))
