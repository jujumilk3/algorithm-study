def solution(food):
    answer = ""
    changed_food = [x // 2 for x in food[1:]]
    print(changed_food)
    for i in range(1, len(changed_food) + 1):
        answer += str(i) * changed_food[i - 1]
    return answer + "0" + answer[::-1]
