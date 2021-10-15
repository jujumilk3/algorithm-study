N, K = map(int, input().split())

foot_prints = [N]
step_counts = [0] * 100001

while foot_prints:
    current = foot_prints.pop(0)
    if current == K:
        print(step_counts[current])
        break
    for j in (current-1, current+1, current*2):
        if 0 <= j <= 100001 and step_counts[j] == 0:
            step_counts[j] = step_counts[current] + 1
            foot_prints.append(j)
