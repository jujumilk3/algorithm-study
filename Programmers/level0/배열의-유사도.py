def solution(s1, s2):
    return len(set(s1) & set(s2))


assert solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]) == 2
assert solution(["n", "omg"], ["m", "dot"]) == 0
