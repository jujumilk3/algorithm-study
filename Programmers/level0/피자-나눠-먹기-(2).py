def solution(n):
    piece = 6
    while True:
        if piece % n == 0:
            return piece // 6
        piece += 6
