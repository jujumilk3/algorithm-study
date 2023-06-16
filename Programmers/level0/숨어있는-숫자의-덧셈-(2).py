import re


def solution(my_string):
    return sum(map(int, re.findall(r"\d+", my_string)))
