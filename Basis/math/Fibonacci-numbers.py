# DP
def fib(n):
    head, body, tail = 0, 1, 0

    for _ in range(n):
        tail = head + body
        head = body
        body = tail
    return head


# Recursive
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
