case_count = int(input())

for case_number in range(1, case_count + 1):
    second = int(input())
    distance = 0
    speed = 0
    for step in range(second):
        command = list(map(int, input().split()))
        if command[0] == 1:
            speed += command[1]
        elif command[0] == 2:
            speed -= command[1]
        if speed < 0:
            speed = 0
        distance += speed
    print('#{} {}'.format(case_number, distance))


"""
10
2
1 2
2 1
3
1 1
0
1 1
5
1 2
1 2
2 1
0
0
8
0
1 2
1 1
0
1 2
2 1
1 1
0
10
1 2
1 1
2 2
1 2
0
0
1 1
1 1
1 2
0
12
1 2
1 1
1 2
2 1
0
1 1
1 1
2 2
2 2
1 1
0
0
15
1 2
1 2
1 2
1 2
1 2
1 2
1 2
1 2
1 2
1 2
1 2
1 2
1 2
1 2
1 2
20
1 2
2 1
0
1 2
0
1 1
2 1
1 2
0
2 1
2 1
0
1 1
0
1 2
1 2
0
1 2
2 2
2 2
25
2 1
2 1
0
0
0
1 2
0
2 2
1 2
2 1
1 1
2 1
0
0
0
1 1
1 2
0
0
1 2
2 2
0
2 2
0
1 1
30
2 1
2 2
2 2
1 1
1 2
2 1
0
1 1
0
0
1 2
1 2
2 1
0
0
2 2
2 1
1 2
0
1 1
2 2
1 2
2 2
0
1 2
2 1
2 2
0
1 1
2 2
"""
