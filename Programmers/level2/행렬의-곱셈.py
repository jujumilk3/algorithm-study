def solution(arr1, arr2):
    x = len(arr2[0])
    y = len(arr1)
    answer = []
    for i in range(y):
        x_list = []
        for j in range(x):
            number = 0
            for k in range(len(arr1[0])):
                nf1 = arr1[i][k]
                nf2 = arr2[k][j]
                number += nf1 * nf2
            x_list.append(number)
        answer.append(x_list)
    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4], [2, 4], [3, 1]]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8]], [[2, 2], [2, 2], [2, 2], [2, 2]]))
