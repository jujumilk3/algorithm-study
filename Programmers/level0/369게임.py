def solution(order):
    return len(str(order)) - len(str(order).replace("3", "").replace("6", "").replace("9", ""))
