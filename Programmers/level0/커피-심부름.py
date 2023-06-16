def solution(order):
    answer = 0
    for menu in order:
        if "america" in menu or "anything" in menu:
            answer += 4500
        elif "latte" in menu:
            answer += 5000
    return answer
