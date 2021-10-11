def solution(sizes):
    widths = []
    heights = []
    for size in sizes:
        if size[0] > size[1]:
            widths.append(size[0])
            heights.append(size[1])
        else:
            widths.append(size[1])
            heights.append(size[0])
    answer = max(widths) * max(heights)
    return answer
# 다른 풀이     return max(max(x) for x in sizes) * max(min(x) for x in sizes)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
