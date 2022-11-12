def solution(my_str, n):
    return [my_str[x: x + n] for x in range(0, len(my_str), n)]


assert solution("abc1Addfggg4556b", 6) == ["abc1Ad", "dfggg4", "556b"]
assert solution("abcdef123", 3) == ["abc", "def", "123"]
