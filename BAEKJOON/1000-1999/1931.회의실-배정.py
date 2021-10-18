time_count = int(input())
times = [list(map(int, input().split())) for _ in range(time_count)]
times.sort(key=lambda x: (x[1], x[0]))
count = 0
current_time = 0
for i in range(time_count):
    if current_time <= times[i][0]:
        current_time = times[i][1]
        count += 1
print(count)
