def solution(arr1, arr2):
    for i, v in enumerate(arr1):
        for i_i, i_v in enumerate(v):
            arr1[i][i_i] = arr1[i][i_i] + arr2[i][i_i]
    return arr1


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
print(solution([[1], [2]], [[3], [4]]))
