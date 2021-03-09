from itertools import combinations


def solution(nums):
    answer = 0
    cmb = list(combinations(nums, 3))
    for number_set in cmb:
        current_number = sum(number_set)
        current_number_prime = True
        for i in range(2, int(current_number ** 0.5) + 1):
            if current_number % i == 0:
                current_number_prime = False
        if current_number_prime:
            answer += 1
    return answer


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
