N_count = int(input())
N = sorted(list(map(int, input().split())))
M_count = int(input())
M = list(map(int, input().split()))


def binary_search(number, start, end):
    if start > end:
        return 0
    center = (start + end) // 2
    if number == N[center]:
        return 1
    elif number < N[center]:
        return binary_search(number, start, center-1)
    else:
        return binary_search(number, center+1, end)


for m in M:
    print(binary_search(m, 0, len(N)-1))
