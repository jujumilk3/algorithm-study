testcase_count = int(input())

for testcase in range(testcase_count):
    k = int(input())
    n = int(input())
    residents = [x for x in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            residents[j] += residents[j-1]
    print(residents[n-1])
