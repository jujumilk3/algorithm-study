def solution(numbers, hand):
    answer = ''
    last_left_finger = '*'
    last_right_finger = '#'
    numpad = {
        1: (1, 1), 2: (2, 1), 3: (3, 1),
        4: (1, 2), 5: (2, 2), 6: (3, 2),
        7: (1, 3), 8: (2, 3), 9: (3, 3),
        '*': (1, 4), 0: (2, 4), '#': (3, 4)
    }
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            last_left_finger = number
        elif number in [3, 6, 9]:
            answer += 'R'
            last_right_finger = number
        else:
            left_finger_x_distance = abs(numpad[number][0] - numpad[last_left_finger][0])
            left_finger_y_distance = abs(numpad[number][1] - numpad[last_left_finger][1])
            left_finger_distance = left_finger_x_distance + left_finger_y_distance
            right_finger_x_distance = abs(numpad[number][0] - numpad[last_right_finger][0])
            right_finger_y_distance = abs(numpad[number][1] - numpad[last_right_finger][1])
            right_finger_distance = right_finger_x_distance + right_finger_y_distance
            if left_finger_distance < right_finger_distance:
                answer += 'L'
                last_left_finger = number
            elif left_finger_distance > right_finger_distance:
                answer += 'R'
                last_right_finger = number
            elif left_finger_distance == right_finger_distance:
                if hand == 'left':
                    answer += 'L'
                    last_left_finger = number
                elif hand == 'right':
                    answer += 'R'
                    last_right_finger = number
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))
