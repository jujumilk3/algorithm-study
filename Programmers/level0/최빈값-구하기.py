from collections import Counter


def solution(array):
    results = Counter(array).most_common(2)
    return results[0][0] if len(results) == 1 or results[0][1] > results[1][1] else -1
