power_list = [5, 3, 1]


def solution(hp):
    answer = 0
    while hp:
        for power in power_list:
            if hp >= power:
                answer += 1
                hp -= power
                break
    return answer
