def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        current_tree_skill = [char for char in tree if char in skill]
        possibility = True
        for i, j in zip(current_tree_skill, skill):
            if i != j:
                possibility = False
                break
        if possibility:
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
