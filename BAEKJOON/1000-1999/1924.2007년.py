months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_weeks = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month, day = list(map(int, input().split()))
day_count = sum(months[:month]) + day
print(day_of_weeks[day_count % 7])
