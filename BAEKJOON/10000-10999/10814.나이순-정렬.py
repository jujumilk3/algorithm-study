users_count = int(input())
users_dict = dict()

for _ in range(users_count):
    info = input().split()
    age = int(info[0])
    name = info[1]
    if age in users_dict:
        users_dict[age].append(name)
    else:
        users_dict[age] = [name]

for age in sorted(users_dict):
    for name in users_dict[age]:
        print(age, name)
