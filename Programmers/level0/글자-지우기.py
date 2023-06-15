def solution(my_string, indices):
    return "".join([x for i, x in enumerate(my_string) if i not in indices])
