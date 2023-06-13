def solution(money):
    answer = [0, 0]
    while money >= 5500:
        answer[0] += 1
        money -= 5500
    answer[1] = money
    return answer
