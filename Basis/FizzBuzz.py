# 1
for number in range(1, 101):
    output = number
    if number % 3 == 0:
        output = 'Fizz'
    if number % 5 == 0:
        output = 'Buzz'
    if number % 15 == 0:
        output = 'FizzBuzz'
    print(output)


# 2
for number in range(1, 101):
    devided = False
    if number % 3 == 0:
        print('Fizz', end='')
        devided = True
    if number % 5 == 0:
        print('Buzz', end='')
        devided = True
    if not devided:
        print(number, end='')


# 3
for number in range(1, 101):
    print('Fizz' * (not number % 3) + 'Buzz' * (not number % 5) or number)


# 4
FizzBuzz = ['Fizz' * (not number % 3) + 'Buzz' * (not number % 5) or number for number in range(1, 100)]
