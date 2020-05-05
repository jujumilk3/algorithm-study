def solution(progresses, speeds):
    answer = []
    day_to_take_list = []
    for progress, speed in zip(progresses, speeds):
        day_to_take = 0
        while True:
            progress += speed
            day_to_take += 1
            if progress > 99:
                break
        day_to_take_list.append(day_to_take)
    print(day_to_take_list)
    current_day_to_take = day_to_take_list[0]
    count_day = 1
    for i in range(1, len(day_to_take_list)):
        print(day_to_take_list[i])
        if current_day_to_take > day_to_take_list[i]:
            count_day += 1
        else:
            current_day_to_take = day_to_take_list[i]
            answer.append(count_day)
            count_day = 1
    answer.append(count_day)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
