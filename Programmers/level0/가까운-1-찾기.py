def solution(arr, idx):
    for index, x in enumerate(arr):
        if index >= idx and arr[index]:
            return index
    return -1
