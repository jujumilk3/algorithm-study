def solution(arr, queries):
    answer = [-1] * len(queries)
    for index, (s, e, k) in enumerate(queries):
        temp_arr = [x for x in arr[s : e + 1] if x > k]
        min_arr = min(temp_arr) if len(temp_arr) else -1
        answer[index] = min_arr
    return answer
