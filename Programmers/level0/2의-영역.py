def solution(arr):
    every_2_indexes = [i for i, x in enumerate(arr) if x == 2]
    try:
        return arr[min(every_2_indexes) : max(every_2_indexes) + 1]
    except Exception:
        return [-1]
