case_count = int(input())

for i in range(case_count):
    scores = list(map(int, input().split()))[1:]
    avg = sum(scores) / len(scores)
    upper = 0
    for score in scores:
        if score > avg:
            upper += 1
    print("%0.3f" % (upper / len(scores) * 100) + '%')


"""
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
"""
