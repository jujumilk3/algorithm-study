number = int(input())

for i in range(number):
    print(' ' * i, end='')
    print('*'*(number-i), end='')
    print('*'*((number-i)-1))

for i in range(2, number+1):
    print(' ' * (number-i), end='')
    print('*' * ((i*2)-1))
