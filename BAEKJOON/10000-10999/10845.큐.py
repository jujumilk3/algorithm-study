from sys import stdin

command_count = int(input())
queue = []

for _ in range(command_count):
    command = stdin.readline().split()
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        print(queue.pop(0) if len(queue) > 0 else -1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(1 if len(queue) == 0 else 0)
    elif command[0] == 'front':
        print(queue[0] if len(queue) > 0 else -1)
    elif command[0] == 'back':
        print(queue[-1] if len(queue) > 0 else -1)
