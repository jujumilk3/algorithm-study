def solution(scores):
    row_and_col = len(scores)
    answer = ''
    for i in range(row_and_col):
        current_student_got_scores = []
        self_score = scores[i][i]
        for j in range(row_and_col):
            current_student_got_scores.append(scores[j][i])
        if current_student_got_scores.count(self_score) == 1:
            if min(current_student_got_scores) == self_score or max(current_student_got_scores) == self_score:
                del current_student_got_scores[current_student_got_scores.index(self_score)]

        if sum(current_student_got_scores) / len(current_student_got_scores) >= 90:
            answer += 'A'
        elif sum(current_student_got_scores) / len(current_student_got_scores) >= 80:
            answer += 'B'
        elif sum(current_student_got_scores) / len(current_student_got_scores) >= 70:
            answer += 'C'
        elif sum(current_student_got_scores) / len(current_student_got_scores) >= 50:
            answer += 'D'
        else:
            answer += 'F'
    return answer


print(solution([[100, 90, 98, 88, 65],
                [50, 45, 99, 85, 77],
                [47, 88, 95, 80, 67],
                [61, 57, 100, 80, 65],
                [24, 90, 94, 75, 65]]))
print(solution([[50, 90], [50, 87]]))
print(solution([[70, 49, 90], [68, 50, 38], [73, 31, 100]]))
