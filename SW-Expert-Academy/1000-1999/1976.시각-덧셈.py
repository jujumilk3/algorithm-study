case_count = int(input())

for i in range(1, case_count + 1):
    input_times = list(map(int, input().split()))
    times = (input_times[0] + input_times[2] + ((input_times[1] + input_times[3]) // 60)) % 12
    minutes = (input_times[1] + input_times[3]) % 60
    times = 12 if times == 0 else times
    print('#{} {} {}'.format(i, times, minutes))


"""
3 
3 17 1 39
8 22 5 10
6 53 2 12   
"""
