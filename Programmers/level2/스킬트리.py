def solution(skill, skill_trees):
    for tree in skill_trees:
        temp_skill = skill
        for skill_in_tree in tree:
            if skill_in_tree == temp_skill[0]:
                print('일치')
            else:
                print('불일치')
    answer = 0
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
