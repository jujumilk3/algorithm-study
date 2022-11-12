def solution(array, height):
    return len([x for x in array if x > height])


assert solution([149, 180, 192, 170], 167) == 3
assert solution([180, 120, 140], 190) == 0
