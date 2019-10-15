def solution(array, commands):
    answer = []
    for command_list in commands:
        managed_list = array[command_list[0]-1: command_list[1]]
        managed_list.sort()
        answer.append(managed_list[command_list[2]-1])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
