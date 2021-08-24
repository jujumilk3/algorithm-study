natural_number_set = set(range(1, 10001))
selfnumber_set = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    selfnumber_set.add(i)

not_self_numbers_set = natural_number_set - selfnumber_set

for i in sorted(not_self_numbers_set):
    print(i)
