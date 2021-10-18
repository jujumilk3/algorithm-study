number = int(input())

head, body, tail = 0, 1, 0

for _ in range(number):
    tail = head + body
    head = body
    body = tail

print(head)
