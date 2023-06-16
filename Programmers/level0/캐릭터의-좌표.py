direction_effect_mapper = {"up": [0, 1], "down": [0, -1], "left": [-1, 0], "right": [1, 0]}


def solution(keyinput, board):
    answer = [0, 0]
    xmin, xmax = board[0] // 2 * -1, board[0] // 2
    ymin, ymax = board[1] // 2 * -1, board[1] // 2
    for key in keyinput:
        answer = [x + y for x, y in zip(answer, direction_effect_mapper[key])]
        x, y = answer
        x = xmax if x > xmax else xmin if x < xmin else x
        y = ymax if y > ymax else ymin if y < ymin else y
        answer = [x, y]
    return answer
