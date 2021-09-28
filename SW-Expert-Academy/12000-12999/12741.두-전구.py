case_count = int(input())
ontimes = []

for case_number in range(1, case_count + 1):
    seconds = list(map(int, input().split()))
    A = [0] * (max(seconds))
    B = [0] * (max(seconds))
    on = 0
    for second in range(seconds[0], seconds[1]):
        A[second] = 1
    for second in range(seconds[2], seconds[3]):
        B[second] = 1
    print(A, B)
    for a, b in zip(A, B):
        if a and b:
            on += 1
    ontimes.append(on)

for index, ontime in enumerate(ontimes):
    print('#', end='')
    print(index+1, ontime)

"""
3
1 3 5 7
0 5 2 4
0 5 1 6
"""
