testcase_count = int(input())
for i in range(testcase_count):
    print(sum(list(map(int, input().split(',')))))
