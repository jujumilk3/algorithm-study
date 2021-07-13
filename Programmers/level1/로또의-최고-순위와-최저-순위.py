def solution(lottos, win_nums):
    zero_count = 0
    match_count = 0
    for lotto_number in lottos:
        if lotto_number == 0:
            zero_count += 1
        for win_num in win_nums:
            if lotto_number == win_num and lotto_number != 0:
                match_count += 1
    best_reward = 7 - (zero_count + match_count)
    worst_reward = 7 - match_count
    worst_reward = 6 if worst_reward > 6 else worst_reward
    best_reward = 6 if best_reward > 6 else best_reward
    return [best_reward, worst_reward]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
print(solution([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]))
