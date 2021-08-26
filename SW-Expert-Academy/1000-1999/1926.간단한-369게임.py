forbidden = ['3', '6', '9']

for i in range(1, int(input())+1):
    number = i
    includes = 0
    for j in forbidden:
        if j in str(i):
            includes += str(i).count(j)

    if includes:
        print('-' * includes, end=' ')
    else:
        print(number, end=' ')
