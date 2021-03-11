from itertools import permutations


def solution(numbers):
    answer = 0
    already_checked = set()
    for i in range(1, len(numbers) + 1):
        for cmb in list(permutations(numbers, i)):
            number = int(''.join(cmb))
            if number in already_checked:
                continue
            already_checked.add(number)
            current_number_prime = True
            for j in range(2, int(number ** 0.5) + 1):
                if number % j == 0:
                    current_number_prime = False
            if number != 1 and number != 0 and current_number_prime:
                answer += 1
    return answer


print(solution("17"))
print(solution("011"))
