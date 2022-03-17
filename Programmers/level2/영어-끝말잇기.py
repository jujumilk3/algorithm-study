from math import ceil


def solution(n, words):
    answer = [0, 0]
    already = []
    index = 0
    for word in words:
        index += 1
        if word in already or (len(already) and already[-1][-1] != word[0]) or len(word) == 1:
            break
        else:
            already.append(word)
    if len(already) != index:
        if index % n == 0:
            wrong = n
        else:
            wrong = index % n
        answer = [wrong, ceil(index / n)]
    return answer


# print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "trim", 'tank']))
print(solution(3, ["tank", "kick", "know",
                   "wheel", "land", "dream",
                   "mother", "robot", "trim",
                   'missant', 'tank']))
# print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(5, ["hello", "observe", "effect", "take", "either",
                   "recognize", "encourage", "ensure", "establish", "hang",
                   "gather", "refer", "reference", "estimate", "executive",
                   "executive"]))
# print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
# print(solution(1, ["hello", "hello"]))
