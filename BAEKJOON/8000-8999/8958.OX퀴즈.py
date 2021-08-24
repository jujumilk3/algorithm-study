testcase_count = int(input())
result_list = []

for testcase_index in range(0, testcase_count):
    ox_input = input()
    current_case_score = 0
    combo_score = 0
    for ox in ox_input:
        if ox == 'O':
            combo_score += 1
        else:
            combo_score = 0
        current_case_score += combo_score
    result_list.append(current_case_score)

print(*result_list)
