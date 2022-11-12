def solution(num, total):
    numbers = list(range(-100, 1000))
    start_index = 0
    while True:
        answer = numbers[start_index: start_index + num]
        if sum(answer) == total:
            break
        else:
            start_index = start_index + 1
    return answer


assert solution(3, 12) == [3, 4, 5]
assert solution(5, 15) == [1, 2, 3, 4, 5]
assert solution(4, 14) == [2, 3, 4, 5]
assert solution(5, 5) == [-1, 0, 1, 2, 3]
