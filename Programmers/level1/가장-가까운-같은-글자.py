def solution(s):
    answer = []
    char_index_dict = {}
    for i, char in enumerate(s):
        if char not in char_index_dict:
            answer.append(-1)
        else:
            answer.append(i - char_index_dict[char])
        char_index_dict[char] = i
    return answer
