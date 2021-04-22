def solution(absolutes, signs):
    for index, sign in enumerate(signs):
        if not sign:
            absolutes[index] = absolutes[index] * -1
    answer = sum(absolutes)
    return answer


print(solution([4, 7, 12], [True, False, True]))
print(solution([1, 2, 3], [False, False, True]))
