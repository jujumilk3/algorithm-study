number_set = set()
for i in range(10):
    number_set.add(divmod(int(input()), 42)[1])
print(len(number_set))
