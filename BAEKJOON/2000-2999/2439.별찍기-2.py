input_number = int(input())
for i in range(1, input_number + 1):
    print(' ' * (input_number - i), end='')
    print('*' * i)
