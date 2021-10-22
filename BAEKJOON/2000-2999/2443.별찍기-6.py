number = int(input())
for i in range(number, -1, -1):
    print(' ' * (number - i), end='')
    print('*' * i, end='')
    print('*' * (i-1), end='')
    print()
