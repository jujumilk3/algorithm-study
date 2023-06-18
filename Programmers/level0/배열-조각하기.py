def solution(arr, query):
    for i, val in enumerate(query):
        if i % 2 == 0:
            del arr[val + 1 :]
        else:
            del arr[:val]
    return arr
