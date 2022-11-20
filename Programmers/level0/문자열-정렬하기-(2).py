def solution(my_string):
    return ''.join(sorted(my_string.lower()))


assert solution("Bcad") == "abcd"
assert solution("heLLo") == "ehllo"
assert solution("Python") == "hnopty"
