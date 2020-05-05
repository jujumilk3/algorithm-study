def solution(A):
    temp_list = {*list(range(1, max(A) + 2))}
    print(temp_list)
    for i in A:
        if i in temp_list:
            temp_list.remove(i)
    return min(temp_list) if temp_list and min(temp_list) > 0 else 1


print(solution([1, 3, 6, 3, 1, 2]))
print()
print(solution([1, 2, 3]))
print()
print(solution([-1, -3]))
