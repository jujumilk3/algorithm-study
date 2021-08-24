input_number = int(input())
for i in range(input_number, 0, -1):
    print(' ' * (input_number - i), end='')
    print('*' * i)
