def solution(cards1, cards2, goal):
    for word in goal:
        if cards1 and word == cards1[0]:
            cards1.pop(0)
        elif cards2 and word == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
