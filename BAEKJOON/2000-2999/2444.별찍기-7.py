number = int(input())

for i in range(1, number):
    print(' ' * (number-i), end='')
    print('*' * ((i*2)-1))

for i in range(number):
    print(' ' * i, end='')
    print('*'*(number-i), end='')
    print('*'*((number-i)-1))

