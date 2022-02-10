order_count = int(input())
deque = []
commands = [input().split() for _ in range(order_count)]
for command in commands:
    if command[0] == 'push_back':
        deque.append(command[1])
    elif command[0] == 'push_front':
        deque.insert(0, command[1])
    elif command[0] == 'pop_front':
        print(deque.pop(0) if len(deque) else -1)
    elif command[0] == 'pop_back':
        print(deque.pop(-1) if len(deque) else -1)
    elif command[0] == 'front':
        print(deque[0] if len(deque) else -1)
    elif command[0] == 'back':
        print(deque[-1] if len(deque) else -1)
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        print(0 if len(deque) else 1)
