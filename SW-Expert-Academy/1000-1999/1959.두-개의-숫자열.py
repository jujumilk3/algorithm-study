case_count = int(input())

for i in range(1, case_count + 1):
    lengths = list(map(int, input().split()))
    results = []
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    movements = max(lengths) - min(lengths)
    longer, shorter = (A, B) if len(A) > len(B) else (B, A)
    shorter_length = len(shorter)
    for move in range(movements+1):
        results.append(sum([x * y for x, y in zip(shorter, longer[move:move+shorter_length])]))
    print('#{} {}'.format(i, max(results)))


"""
10
3 5
1 5 3
3 6 -7 5 4
7 6
6 0 5 5 -1 1 6
-4 1 8 7 -9 3
5 15
-8 4 6 -9 -1
-1 1 0 -2 10 10 0 2 5 2 10 7 -9 7 -8
11 20
3 -8 4 0 -1 -4 8 3 7 -3 1
3 10 0 1 10 0 -8 -6 9 -7 -1 1 -1 4 10 6 0 -8 -5 0
11 16
-6 0 -1 7 5 -1 -3 0 -9 8 4
0 -6 1 1 8 -8 0 -7 4 -7 -8 -2 1 4 0 -10
3 16
8 9 0
-4 9 -7 -1 -8 3 1 -6 -8 5 2 -7 -9 -10 8 9
11 3
3 -4 -7 7 -2 5 5 0 -2 -8 4
-1 1 3
14 6
-9 9 0 -7 8 10 7 -3 2 3 0 0 0 -2
8 1 -9 3 0 -7
17 10
-6 -1 -4 2 -5 1 -10 -9 8 -9 -6 1 10 0 -5 -8 1
7 6 2 7 -8 4 8 10 -2 9
11 9
8 6 -2 0 0 5 10 2 -10 -8 -10
10 -9 -7 -1 0 8 0 10 3
"""
