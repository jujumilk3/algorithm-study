def solution(scoville, K):
    answer = 0
    scoville.sort(reverse=True)
    while min(scoville) < K:
        first = scoville.pop()
        second = scoville.pop()
        new = first + (second * 2)
        scoville.append(new)
        scoville.sort(reverse=True)
        answer += 1
        print(scoville, first, second, new)
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 1, 1, 1], 7))
