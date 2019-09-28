def solution(d, budget):
    answer = 0
    d.sort()
    for cost in d:
        budget -= cost
        answer += 1
        if budget < 0:
            answer -= 1
            break
    return answer


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))
