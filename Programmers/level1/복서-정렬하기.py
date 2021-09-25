def solution(weights, head2head):
    match_count = len(head2head[0]) - 1
    answer = []
    heavy_counts = [0] * len(weights)
    win_rates = [0] * len(weights)
    print(heavy_counts)
    print(win_rates)
    for index, results in enumerate(head2head):
        print(results)
        print(results.count('W'))
        print('win rate:', results.count('W') / match_count)
        print(weights[index])

    return answer


print(solution([50, 82, 75, 120], ['NLWL', 'WNLL', 'LWNW', 'WWLN']))
print(solution([145, 92, 86], ['NLW', 'WNL', 'LWN']))
print(solution([60, 70, 60], ['NNN', 'NNN', 'NNN']))
