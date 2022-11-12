words = ["aya", "ye", "woo", "ma"]


def solution(babblings):
    answer = 0
    for babbling in babblings:
        current_babbling = babbling
        for word in words:
            current_babbling = current_babbling.replace(word, "-")
        if len(current_babbling.replace("-", "")) == 0:
            answer += 1
    return answer


assert solution(["aya", "yee", "u", "maa", "wyeoo"]) == 1
assert solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]) == 3
