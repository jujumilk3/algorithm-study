def solution(common):
    num = common[1] - common[0]
    if (common[1] - common[0]) == num:
        answer = common[len(common)-1] + num
    else:
        num = common[1] // common[0]
        answer = common[len(common)-1] * num
    return answer


assert solution([1, 2, 3, 4]) == 5
assert solution([2, 4, 8]) == 16
assert solution([3, 9, 27]) == 81
