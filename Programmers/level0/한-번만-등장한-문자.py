from collections import defaultdict


def solution(s):
    answer = []
    count_dict = defaultdict(int)
    for char in s:
        count_dict[char] += 1
    for k, v in count_dict.items():
        if v == 1:
            answer.append(k)
    return "".join(sorted(answer))
