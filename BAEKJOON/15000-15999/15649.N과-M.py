from itertools import permutations
N, M = map(int, input().split())
perms = permutations(range(1, N+1), M)
for perm in perms:
    print(' '.join(list(map(str, perm))))
