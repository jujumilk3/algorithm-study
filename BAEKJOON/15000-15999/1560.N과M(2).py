from itertools import combinations
N, M = map(int, input().split())
N = range(1, N+1)
perms = combinations(N, M)
for perm in perms:
    print(' '.join(map(str, perm)))
