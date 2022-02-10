n = int(input())
stack = []
for _ in range(n):
    number = int(input())
    if number != n:
        stack.append(number)
        print('+')
    else:
        print('-')
        n -= 1
    print(stack)
