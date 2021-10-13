number = int(input())
for i in range(1, number+1):
    print(' ' * (number-i), end='')
    print('*' * ((i*2)-1))
