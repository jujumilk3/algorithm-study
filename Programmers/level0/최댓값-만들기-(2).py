def solution(numbers):
    sorted_numbers = sorted(numbers)
    return max(sorted_numbers[0] * sorted_numbers[1], sorted_numbers[-1] * sorted_numbers[-2])
