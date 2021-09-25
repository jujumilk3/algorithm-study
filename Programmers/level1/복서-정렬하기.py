def solution(weights, head2head):
    info = []
    players_count = len(weights)
    for p in range(players_count):
        high = [i for i in range(players_count) if weights[i] > weights[p]]
        over = len([info for info in high if head2head[p][info] == 'W'])
        rate = 0 if not head2head[p].count('W') else head2head[p].count('W') / (players_count - head2head[p].count('N'))
        info.append((p, weights[p], rate, over))
    info = sorted(info, key=lambda x: (x[2], x[3], x[1], -x[0]), reverse=True)
    return [num[0] + 1 for num in info]


print(solution([50, 82, 75, 120], ['NLWL', 'WNLL', 'LWNW', 'WWLN']))
print(solution([145, 92, 86], ['NLW', 'WNL', 'LWN']))
print(solution([60, 70, 60], ['NNN', 'NNN', 'NNN']))
