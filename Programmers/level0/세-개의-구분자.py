import re


def solution(myStr):
    return [x for x in re.split("a|b|c", myStr) if x] or ["EMPTY"]
