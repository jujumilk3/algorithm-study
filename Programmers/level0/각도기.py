def solution(angle):
    return 1 if angle < 90 else 2 if angle == 90 else 3 if 90 < angle < 180 else 4
