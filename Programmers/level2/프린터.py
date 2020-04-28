def solution(priorities, location):
    prio_dict = {i: priorities[i] for i in range(len(priorities))}
    for i in range(len(prio_dict)):
        print(prio_dict)
        for j in range(i+1, len(prio_dict)):
            print(i, "와", j)
            if prio_dict[i] < prio_dict[j]:
                temp_k = i
                temp_v = prio_dict[i]
                del prio_dict[i]
                prio_dict[temp_k] = temp_v

    # i부터 끝까지가 아니라 계속해서 처음부터 조사하되
    # 각 요소의 뒤에 더 큰게 나타날 때마다 해당 요소를 뒤로 보내고 처음부터 시작.
    # 처음부터 끝까지 조사했을 때 뒤에 더 큰게 없으면 정렬을 종료.
    return list(prio_dict.keys()).index(location) + 1


# print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([2, 1, 2, 3], 2))
