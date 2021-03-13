def solution(n):
    # 1
    res = [[0] * n for _ in range(n)]
    answer = []
    y, x = -1, 0
    num = 1

    # 2
    # 값을 채우는 것은 세방향이니까 i % 3으로 방향을 결정.
    # range(i, n)을 하면 외부 반복문이 시작된 수에서 다시 시작되니까 방향이 정해지는 거임...
    for i in range(n):
        for j in range(i, n):
            print(i, j)
            # 3
            # down
            if i % 3 == 0:
                y += 1

            # right
            elif i % 3 == 1:
                x += 1

            # up
            elif i % 3 == 2:
                x -= 1
                y -= 1
            # 4
            print(x, y, i % 3)
            res[y][x] = num
            num += 1
            print()
    print(res)
    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer


print(solution(4))
print(solution(5))
print(solution(6))
