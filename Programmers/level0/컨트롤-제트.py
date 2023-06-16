def solution(s):
    stack = []
    for num in s.split():
        try:
            stack.append(int(num))
        except:
            stack.pop()
    return sum(stack)
