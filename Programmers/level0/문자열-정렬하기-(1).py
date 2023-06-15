def solution(my_string):
    return sorted(map(int, list(filter(str.isdigit, my_string))))
