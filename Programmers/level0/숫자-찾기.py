def solution(num, k):
    try:
        return str(num).index(str(k)) + 1
    except:
        return -1


assert solution(29183, 1) == 3
assert solution(232443, 4) == 4
assert solution(123456, 7) == -1
